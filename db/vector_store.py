import faiss
import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
DIM = 384
STORE_PATH = "data/history.pkl"

model = SentenceTransformer(MODEL_NAME)

index = faiss.IndexFlatL2(DIM)
memory = []

def load_memory():
    global index, memory
    if os.path.exists(STORE_PATH):
        try:
            with open(STORE_PATH, "rb") as f:
                index, memory = pickle.load(f)
        except:
            index = faiss.IndexFlatL2(DIM)
            memory = []
    else:
        index = faiss.IndexFlatL2(DIM)
        memory = []

import os

def save_memory():
    os.makedirs("data", exist_ok=True)  # ✅ auto-create folder
    with open(STORE_PATH, "wb") as f:
        pickle.dump((index, memory), f)

def add_to_memory(prompt, failure, fix):
    record = {
        "prompt": prompt,
        "failure": failure,
        "fix": fix
    }

    text = f"{prompt} {failure} {fix}"

    embedding = model.encode([text])
    embedding = np.array(embedding).astype("float32")

    index.add(embedding)
    memory.append(record)

    save_memory()

def search_similar(query, k=3):
    if len(memory) == 0:
        return []

    embedding = model.encode([query])
    embedding = np.array(embedding).astype("float32")

    D, I = index.search(embedding, k)

    results = []
    for idx in I[0]:
        if idx < len(memory):
            item = memory[idx]
            formatted = f"""
Prompt: {item['prompt']}
Failure: {item['failure']}
Fix: {item['fix']}
"""
            results.append(formatted)

    return results