import logging
import os
from typing import List, Optional

from langchain_community.tools import (
    BraveSearch,
    DuckDuckGoSearchResults,
    SearxSearchRun,
    WikipediaQueryRun,
)
from langchain_community.tools.arxiv import ArxivQueryRun
from langchain_community.utilities import (
    ArxivAPIWrapper,
    BraveSearchWrapper,
    SearxSearchWrapper,
    WikipediaAPIWrapper,
)

from config import SELECTED_SEARCH_ENGINE, SearchEngine, load_yaml_config
from tools.decorators import create_logged_tool

logger = logging.getLogger(__name__)

# Create logged versions of the search tools
LoggedDuckDuckGoSearch = create_logged_tool(DuckDuckGoSearchResults)


def get_search_config():
    config = load_yaml_config("conf.yaml")
    search_config = config.get("SEARCH_ENGINE", {})
    return search_config


# Get the selected search tool
def get_web_search_tool(max_search_results: int):
    # Log the selected search engine
    logger.info(f"Using search engine: {SELECTED_SEARCH_ENGINE}")
    
    if SELECTED_SEARCH_ENGINE == SearchEngine.TAVILY.value:
        from langchain_community.tools.tavily_search import TavilySearchResults
        return create_logged_tool(TavilySearchResults)(
            name="web_search",
            max_results=max_search_results,
        )
    elif SELECTED_SEARCH_ENGINE == SearchEngine.DUCKDUCKGO.value:
        return LoggedDuckDuckGoSearch(
            name="web_search",
            num_results=max_search_results,
        )
    else:
        # Default fallback to DuckDuckGo or raise error
        logger.warning(f"Unknown search engine '{SELECTED_SEARCH_ENGINE}', falling back to DuckDuckGo")
        return LoggedDuckDuckGoSearch(
            name="web_search",
            num_results=max_search_results,
        )
