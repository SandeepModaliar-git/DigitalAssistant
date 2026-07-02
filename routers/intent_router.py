from typing import Literal
from pydantic import BaseModel
from llm.simple_model import get_llm_client
from graph.state import AgentState

class Intent(BaseModel):
    intent: Literal["READ", "WRITE"]

def intent_router(state: AgentState) -> AgentState:
    llm = get_llm_client(model="gpt-4o-mini")
    structured_llm = llm.with_structured_output(Intent)
    query = state["query"]
    prompt = f"""
    You are an intent classifier for a Supply Chain Control Tower.
    
    Classify the user's request as one of the following:
    
    READ
    - Retrieve information
    - Ask questions
    - Analyze data
    - View shipment status
    - Check inventory
    - Generate reports
    - Explain information
    
    WRITE
    - Modify data
    - Trigger workflows
    - Reroute shipments
    - Update inventory
    - Create tickets
    - Notify customers
    - Cancel shipments
    - Approve or reject requests
    
    Return ONLY the intent.
    
    User Query:
    {query}
    """
    response = structured_llm.invoke(prompt)

    return {"intent": response.intent, "messages": [f"Intent Classified as {response.intent}"]}