from langchain_community.chat_models import ChatOllama
import tools
import os
import json
import pprint
from logger import log_response

ollama_model = os.getenv("OLLAMA_MODEL_NAME", "mistral")
llm = ChatOllama(model=ollama_model)

print("Model:", ollama_model)

def agent(prompt: str):
    # Step 1: Reason with LLM
    response = llm.invoke(prompt)
    print("LLM says:", response)

    # Step 2: Dispatch to tools based on keywords
    if "resume" in prompt.lower():
        files = tools.list_resumes()
        print("Local action: found resumes ->", files)

    elif "count" in prompt.lower() and "txt" in prompt.lower():
        count = tools.count_files(extension=".txt")
        print("Local action: counted txt files ->", count)

    elif "fetch" in prompt.lower():
        # Example: "fetch file C:/Users/xyz/Documents/test.txt"
        parts = prompt.split()
        for p in parts:
            if p.startswith("C:/"):
                content = tools.fetch_file(p)
                print("Local action: file content ->", content[:200], "...")