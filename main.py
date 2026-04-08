import streamlit as st
import ollama 
import os
import chromadb

folder_path = "data"

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.create_collection("energy_logs")


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
for i,filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(".txt"):
        
        # reading the file
        with open(os.path.join(folder_path,filename) , "r") as f :
            text = f.read()
            
        chunks = chunk_text(text)
        for chunk in chunks:
            #  embedding
            response = ollama.embed(
            model="nomic-embed-text-v2-moe",
            input = text
            )
            embedding = response["embeddings"]
        
            collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[str(i)]
            )
            doc_id +=1
        
client.persist()   
print("✅ All files embedded and stored!")
        
        
        
