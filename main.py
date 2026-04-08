import streamlit as st
import ollama
import os
import chromadb

folder_path = "data"

# ✅ persistent DB
client = chromadb.PersistentClient(path="./chroma_db")

# ✅ safe collection creation
collection = client.get_or_create_collection("energy_logs")


#  ------------------- DATA Agent ----------------------------------------------------------
# 🔧 chunk function
def chunk_text(text, chunk_size=400, overlap=50):
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    
    return chunks

doc_id = 0

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        
        with open(os.path.join(folder_path, filename), "r") as f:
            text = f.read()
        
        chunks = chunk_text(text)

        for chunk in chunks:
            # ✅ embedding on chunk
            response = ollama.embed(
                model="nomic-embed-text-v2-moe",
                input=chunk
            )
            
            embedding = response["embeddings"][0]

            collection.add(
                documents=[chunk],
                embeddings=[embedding],
                ids=[f"{filename}_{doc_id}"]  # ✅ unique ID
            )

            doc_id += 1

# (PersistentClient auto-saves, no need persist)

st.title("Energy AI Assistant")

#  -----  --------- End of Data Agent

#----------------------  Start of Analysis Agent

query = st.text_input("Enter your Query")
if (st.button("Ask") and query):
    query_embedding = ollama.embed(
        model="nomic-embed-text-v2-moe",
        input=query
    )["embeddings"][0]
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )
    relevant_docs = results["documents"][0]
    
    #  ------ End of Analysis Agent

    # ------- Start of Report Agent
    # 🔹 4. Create context
    context = "\n".join(relevant_docs)
    
    response = ollama.chat(
        model="ministral-3:3b",
        messages=[
            {
                "role": "user",
                "content": f"""
    You are an energy analysis assistant.

    Use the following logs to answer the question clearly and accurately.

    Logs:
    {context}

    Question:
    {query}

    Answer:
    """
            }
        ]
    )
    
    # 🔹 5. Show final answer
    st.subheader("🤖 AI Answer:")
    st.write(response["message"]["content"])
    st.subheader("🔍 Relevant Logs:")
    for doc in relevant_docs:
        st.write(doc)

    