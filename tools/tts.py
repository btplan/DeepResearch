"""
Text-to-Speech module using volcengine TTS API.
"""

import json
import logging
import os
import uuid
from typing import Any, Dict, Optional

from dotenv import load_dotenv
import requests

load_dotenv()

logger = logging.getLogger(__name__)


def _env_or_value(value: Optional[str], env_name: str, required: bool = True) -> str:
    resolved = value or os.getenv(env_name)
    if resolved:
        return resolved.strip()
    if required:
        raise ValueError(f"Missing required environment variable: {env_name}")
    return ""


class VolcengineTTS:
    """
    Client for volcengine Text-to-Speech API.
    """

    def __init__(
        self,
        appid: Optional[str] = None,
        access_token: Optional[str] = None,
        cluster: Optional[str] = None,
        voice_type: Optional[str] = None,
        host: Optional[str] = None,
        api_url: Optional[str] = None,
    ):
        """
        Initialize the volcengine TTS client.

        Args:
            appid: Platform application ID
            access_token: Access token for authentication
            cluster: TTS cluster name
            voice_type: Voice type to use
            host: API host
            api_url: Full API URL. If provided, it takes precedence over host.
        """
        self.appid = _env_or_value(appid, "VOLCENGINE_TTS_APPID")
        self.access_token = _env_or_value(access_token, "VOLCENGINE_TTS_ACCESS_TOKEN")
        self.cluster = _env_or_value(cluster, "VOLCENGINE_TTS_CLUSTER")
        self.voice_type = _env_or_value(voice_type, "VOLCENGINE_TTS_VOICE_TYPE")
        self.host = _env_or_value(host, "VOLCENGINE_TTS_HOST", required=False)
        self.api_url = _env_or_value(api_url, "VOLCENGINE_TTS_API_URL")
        self.header = {"Authorization": f"Bearer;{self.access_token}"}

    def text_to_speech(
        self,
        text: str,
        encoding: str = "mp3",
        speed_ratio: float = 1.0,
        volume_ratio: float = 1.0,
        pitch_ratio: float = 1.0,
        text_type: str = "plain",
        with_frontend: int = 1,
        frontend_type: str = "unitTson",
        uid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Convert text to speech using volcengine TTS API.

        Args:
            text: Text to convert to speech
            encoding: Audio encoding format
            speed_ratio: Speech speed ratio
            volume_ratio: Speech volume ratio
            pitch_ratio: Speech pitch ratio
            text_type: Text type (plain or ssml)
            with_frontend: Whether to use frontend processing
            frontend_type: Frontend type
            uid: User ID (generated if not provided)

        Returns:
            Dictionary containing the API response and base64-encoded audio data
        """
        if not uid:
            uid = str(uuid.uuid4())

        request_json = {
            "app": {
                "appid": self.appid,
                "token": self.access_token,
                "cluster": self.cluster,
            },
            "user": {"uid": uid},
            "audio": {
                "voice_type": self.voice_type,
                "encoding": encoding,
                "speed_ratio": speed_ratio,
                "volume_ratio": volume_ratio,
                "pitch_ratio": pitch_ratio,
            },
            "request": {
                "reqid": str(uuid.uuid4()),
                "text": text,
                "text_type": text_type,
                "operation": "query",
                "with_frontend": with_frontend,
                "frontend_type": frontend_type,
            },
        }

        try:
            sanitized_text = text.replace("\r\n", "").replace("\n", "")
            logger.debug(f"Sending TTS request for text: {sanitized_text[:50]}...")
            response = requests.post(
                self.api_url, json.dumps(request_json), headers=self.header
            )
            response_json = response.json()

            if response.status_code != 200:
                logger.error(f"TTS API error: {response_json}")
                return {"success": False, "error": response_json, "audio_data": None}

            if "data" not in response_json:
                logger.error(f"TTS API returned no data: {response_json}")
                return {
                    "success": False,
                    "error": "No audio data returned",
                    "audio_data": None,
                }

            return {
                "success": True,
                "response": response_json,
                "audio_data": response_json["data"],  # Base64 encoded audio data
            }

        except Exception as e:
            logger.exception(f"Error in TTS API call: {str(e)}")
            return {"success": False, "error": "TTS API call error", "audio_data": None}
