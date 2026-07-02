from typing import Literal
from pydantic import BaseModel
from llm.simple_model import get_llm_client

class GuardrailDecision(BaseModel):
    action: Literal["ALLOW", "BLOCK"]
    reason: str

guardrail_prompt = """
    You are a security guardrail.
    
    Determine whether the user is attempting to perform
    an action that changes enterprise data or triggers
    a business workflow.
    
    Examples of WRITE:
    
    - reroute shipment
    - create ticket
    - notify customers
    - update inventory
    - cancel shipment
    - approve order
    - reject request
    - delete shipment
    - modify order
    
    Examples of READ:
    
    - where is shipment
    - show inventory
    - explain delay
    - summarize carrier performance
    - why is shipment delayed
    
    If WRITE:
    Return BLOCK
    
    If READ:
    Return ALLOW
    """

def security_guardrail(query: str):
    llm = get_llm_client(model="gpt-4o-mini")
    structured_llm = llm.with_structured_output(GuardrailDecision)
    result = structured_llm.invoke(
        guardrail_prompt + f"\n\nUser Query:\n{query}"
    )
    return result