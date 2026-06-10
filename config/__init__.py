from dotenv import load_dotenv

from .loader import load_yaml_config
from .tools import SELECTED_SEARCH_ENGINE, SearchEngine

# Load environment variables
load_dotenv()


__all__ = [
    # Other configurations
    "SELECTED_SEARCH_ENGINE",
    "SearchEngine",
    load_yaml_config,
]
