from graph.state import AgentState
from llm.simple_model import get_llm_client
import os
import re

def sql_query_generation_agent(state: AgentState):
    schema_context = state["schema_context"]
    user_query = state["query"]
    sql_prompt = f"""
    You are an expert PostgreSQL SQL generator for a Supply Chain Digital Assistant.

    Your task is to generate a syntactically correct PostgreSQL query based ONLY on the provided schema context.

    ## Schema Context
    {schema_context}

    ## User Question
    {user_query}

    ## Instructions

    1. Use ONLY the tables and columns present in the Schema Context.
    2. Do NOT invent tables, columns, or relationships.
    3. Use the example SQL only as a reference for style. Do not copy it unless it exactly answers the question.
    4. If multiple columns could satisfy the request, choose the most semantically relevant one based on the descriptions and synonyms.
    5. If filters are required, infer them from the user's question.
    6. Return only a valid PostgreSQL SQL query.
    7. Do not include markdown, explanations, comments, or any additional text.
    8. If the schema context is insufficient to answer the question, return exactly:

    INSUFFICIENT_SCHEMA

    SQL:
    """
    llm = get_llm_client(os.environ["MODEL"])
    response = llm.invoke(sql_prompt)
    sql = re.sub(r"^```(?:sql)?|```$", "", response.content.strip(), flags=re.MULTILINE).strip()
    return {
        "sql_query": sql,
        "schema_context": None,
        "messages": ["SQL Query Generated!"]
    }
