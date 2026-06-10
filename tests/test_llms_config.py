import importlib.util
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


class LLMConfigTests(unittest.TestCase):
    def tearDown(self):
        sys.modules.pop("agents.llms", None)

    @patch.dict(
        os.environ,
        {
            "LLM_BASE_URL": "https://example.test/v1",
            "LLM_API_KEY": "test-key",
            "LLM_MODEL": "test-model",
            "LLM_TEMPERATURE": "0.3",
        },
        clear=False,
    )
    def test_get_llm_uses_environment_configuration(self):
        with patch("langchain_openai.ChatOpenAI") as chat_openai:
            module_path = Path(__file__).resolve().parents[1] / "agents" / "llms.py"
            spec = importlib.util.spec_from_file_location("llms_under_test", module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.get_llm()

        chat_openai.assert_called_once_with(
            base_url="https://example.test/v1",
            api_key="test-key",
            model="test-model",
            temperature=0.3,
        )


if __name__ == "__main__":
    unittest.main()
