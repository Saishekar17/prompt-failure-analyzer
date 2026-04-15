import ollama

MODEL = "phi3"  # 🔥 change from llama3 → phi3

def generate(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={
            "num_predict": 200  # limit output → saves memory
        }
    )
    return response["message"]["content"]