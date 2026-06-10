import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

_llm = None


def _required_env(name: str, fallback_name: str | None = None) -> str:
    value = os.getenv(name)
    if value:
        return value.strip()
    if fallback_name:
        fallback_value = os.getenv(fallback_name)
        if fallback_value:
            return fallback_value.strip()
    raise ValueError(f"Missing required environment variable: {name}")


def _float_env(name: str) -> float:
    value = _required_env(name)
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be a float value, got: {value}") from exc


def get_llm():
    global _llm
    if _llm is None:
        _llm = ChatOpenAI(
            base_url=_required_env("LLM_BASE_URL"),
            api_key=_required_env("LLM_API_KEY", "DASHSCOPE_API_KEY"),
            model=_required_env("LLM_MODEL"),
            temperature=_float_env("LLM_TEMPERATURE"),
        )
    return _llm
