from graph.state import AgentState
import os
from sqlalchemy import create_engine
from sqlalchemy import text

def sql_executor_agent(state: AgentState):
    sql_query = state["sql_query"]
    DATABASE_URL = os.environ["DATABASE_URL"]
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
        echo=False
    )
    with engine.connect() as conn:
        result = conn.execute(text(sql_query))
        rows = result.mappings().all()

    return {
        "query_result": rows,
        "messages": ["SQL Executed Successfully!"]
    }

