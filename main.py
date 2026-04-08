import streamlit as st
import ollama 
import os
import chromadb

folder_path = "data"
client = chromadb.Client()

collection = client.create_collection("energy_logs")


for i,filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(".txt"):
        
        # reading the file
        with open(os.path.join(folder_path,filename) , "r") as f :
            text = f.read()
        
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
        
print("✅ All files embedded and stored!")
        
        
        
