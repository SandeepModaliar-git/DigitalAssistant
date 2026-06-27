import os
from langchain_openai import ChatOpenAI
from openai import OpenAI

def get_llm_client(model):
    print("Loading LLM model...", model)
    return ChatOpenAI(
        model=model,
        openai_api_key=os.environ.get("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )

def get_embedding_client():
    return OpenAI(
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
    )