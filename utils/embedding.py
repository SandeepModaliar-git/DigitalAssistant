from llm.simple_model import get_embedding_client
import os

def get_embedding(text):
    embedding_client = get_embedding_client()
    response = embedding_client.embeddings.create(
        model=os.environ.get("EMBEDDING_MODEL"),
        input=text,
        dimensions=1024
    )
    return response.data[0].embedding