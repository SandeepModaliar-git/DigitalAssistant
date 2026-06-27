from graph.state import AgentState
import json

def context_generation_agent(state: AgentState):
    metadata_results = state["metadata_results"]
    try:
        documents = []
        for result in metadata_results:
            documents.append(json.loads(result["table"]))
        schema_context = []
        for doc in documents:
            if "column" in doc:
                schema_context.append(f"""
        Table: {doc['table']}
    
        Column: {doc['column']}
    
        Description:
        {doc['description']}
    
        Synonyms:
        {chr(10).join(doc.get('aliases', []))}
        """)

            elif "columns" in doc:

                schema_context.append(f"""
        Table: {doc['table']}
    
        Description:
        {doc['description']}
    
        Columns:
        {", ".join(doc['columns'])}
        """)

            elif "sql" in doc:

                schema_context.append(f"""
        Example Question:
        {doc['question']}
    
        Example SQL:
        {doc['sql']}
        """)
        schema_context = "\n\n".join(schema_context)
        return {"schema_context": schema_context, "messages": ["Schema Context Generated!"], "metadata_results": None}
    except Exception as e:
        return {"schema_context": "", "messages": ["Schema Context Generation Failed!"],  "metadata_results": None}
