from graph.state import AgentState
from langgraph.graph import StateGraph, START, END
from agents.metadata_retrieval_agent import metadata_retrieval_agent
from agents.context_generation_agent import context_generation_agent
from agents.sql_query_generation_agent import sql_query_generation_agent
from pprint import pprint
from utils.env import load_project_env

load_project_env()
workflow = StateGraph(AgentState)

workflow.add_node("metadata_retrieval", metadata_retrieval_agent)
workflow.add_node("context_generation", context_generation_agent)
workflow.add_node("sql_query_generation", sql_query_generation_agent)

workflow.set_entry_point("metadata_retrieval")
workflow.add_edge("metadata_retrieval", "context_generation")
workflow.add_edge("context_generation", "sql_query_generation")
workflow.add_edge("sql_query_generation", END)

app = workflow.compile()
results = app.invoke({"query": "Where is shipment SHP123?"})

print(results["sql_query"])