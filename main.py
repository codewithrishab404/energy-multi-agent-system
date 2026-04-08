import streamlit as st
import ollama
import os
import chromadb

folder_path = "data"

# ✅ persistent DB
client = chromadb.PersistentClient(path="./chroma_db")

# ✅ safe collection creation
collection = client.get_or_create_collection("energy_logs")

# 🔧 chunk function
def chunk_text(text, chunk_size=300, overlap=50):
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

query = st.text_input("Enter your Query")

    

    