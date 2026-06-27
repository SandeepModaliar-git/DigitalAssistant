from typing import TypedDict, Annotated
from langgraph.graph import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    metadata_results: list[dict]
    query: str
    schema_context: str
    sql_query: str
    query_result: list[dict[str, str]]


