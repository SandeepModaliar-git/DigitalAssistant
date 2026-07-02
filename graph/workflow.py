from agents.write_agent import write_agent
from graph.state import AgentState
from langgraph.graph import StateGraph, START, END
from agents.metadata_retrieval_agent import metadata_retrieval_agent
from agents.context_generation_agent import context_generation_agent
from agents.sql_query_generation_agent import sql_query_generation_agent
from agents.sql_executor_agent import sql_executor_agent
from routers.intent_router import intent_router

from utils.env import load_project_env

load_project_env()
workflow = StateGraph(AgentState)

workflow.add_node("metadata_retrieval", metadata_retrieval_agent)
workflow.add_node("context_generation", context_generation_agent)
workflow.add_node("sql_query_generation", sql_query_generation_agent)
workflow.add_node("sql_executor", sql_executor_agent)
workflow.add_node("write_agent", write_agent)
workflow.add_node("intent_router", intent_router)

workflow.set_entry_point("intent_router")
workflow.add_conditional_edges(
    "intent_router",
    lambda state: state["intent"],
    {
        "READ": "metadata_retrieval",
        "WRITE": "write_agent"
    }
)

workflow.add_edge("metadata_retrieval", "context_generation")
workflow.add_edge("context_generation", "sql_query_generation")
workflow.add_edge("sql_query_generation", "sql_executor")
workflow.add_edge("sql_executor", END)

app = workflow.compile()
results = app.invoke({"query": "update the shipment status for SHIP-12345 to 'delayed' and notify the customer."})

print(results.get("sql_query", ""))
print(results.get("query_result", ""))
print(results.get("intent", ""))
print(results.get("messages", [])[-1].content)