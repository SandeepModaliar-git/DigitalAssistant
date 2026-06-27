import os
from pinecone import Pinecone

def pinecone_client():
    return Pinecone(api_key=os.environ["PINECONE_API_KEY"])

def pinecone_index():
    pc = pinecone_client()
    index = pc.Index("text-to-sql")
    return index