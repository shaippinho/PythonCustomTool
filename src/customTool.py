from langchain.tools import tool


@tool
def search_api(query: str) -> str:
    """Searches the API for the query."""
    # return f"Results for query {query}"
    return f"The Age is 40"
