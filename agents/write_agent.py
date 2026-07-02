from graph.state import AgentState

def write_agent(state: AgentState) -> dict:
    return {
        "query": state["query"],
        "messages" : ["This is a write operation. This assistant only supports read-only operations."]
    }