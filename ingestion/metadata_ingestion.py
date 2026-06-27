from utils.env import load_project_env
from llm.simple_model import get_llm_client
from ingestion.metadata_documents import documents
import os
import json
from utils.pinecone import pinecone_client
from utils.embedding import get_embedding

def generate_vectors(docs):
    vectors = []
    for doc in docs:
        text = json.dumps(doc["text"])
        embedding = get_embedding(text)
        vectors.append({
            "id": doc["id"],
            "values": embedding,
            "metadata": {
                "type": doc["type"],
                "text": text
            }
        })
    return vectors

def ingest_embeddings(doc_index, vectors):
    try:
        doc_index.upsert(vectors=vectors)
        print("Documents stored successfully!")
    except Exception as e:
        print("Documents not stored successfully!", e)

def retrieve_metadata(doc_index, query):
    try:
        embedding = get_embedding(query)
        results = doc_index.query(
            vector=embedding,
            top_k=5,
            include_metadata=True
        )
        for match in results["matches"]:
            print(match)
            print(match["score"])
            print(match["metadata"]["text"])
        print("Document retrieved successfully!")
    except Exception as e:
        print("Document retrieval failed!")

if __name__ == "__main__":
    load_project_env()
    pc = pinecone_client()
    llm_model = os.environ.get("MODEL")
    index = pc.Index("text-to-sql")
    print(llm_model)
    llm = get_llm_client(llm_model)
    embeddings = generate_vectors(documents)
    ingest_embeddings(index, embeddings)
    retrieve_metadata(index, "Where is shipment SHP123?")
