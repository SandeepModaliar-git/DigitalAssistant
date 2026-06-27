import traceback
from graph.state import AgentState
from utils.embedding import get_embedding
from utils.pinecone import pinecone_index


def metadata_retrieval_agent(state: AgentState):
    query = state.get("query")
    metadata_results = []
    try:
        embedding = get_embedding(query)
        doc_index = pinecone_index()
        results = doc_index.query(vector=embedding, top_k=5, include_metadata=True)
        print(results)
        for match in results["matches"]:
            metadata_results.append(
                {"table": match["metadata"]["text"], "score": match["score"]}
            )
        return {
            "messages": ["Metadata retrieval successful!"],
            "metadata_results": metadata_results,
        }
    except Exception as e:
        traceback.print_exc()
        return {"messages": ["Metadata retrieval failed!"], "metadata_results": []}
