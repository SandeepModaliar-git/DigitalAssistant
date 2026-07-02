from guardrails.security_guardrail import security_guardrail
from graph.state import AgentState

def guardrail_agent(state: AgentState) -> dict:
    decision = security_guardrail(state["query"])
    if decision.action == "BLOCK":
        return {
            "response":
                "This assistant only supports read-only operations."
        }
    return {}