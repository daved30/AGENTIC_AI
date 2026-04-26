from langchain_community.chat_models import ChatOllama
import json
import os
import re

print("|| Planner Agent ||")
ollama_model = os.getenv("OLLAMA_MODEL_NAME", "llama3.1:8b")
llm = ChatOllama(model=ollama_model, temperature=0) # Temp 0 makes it more consistent

print("Model:", ollama_model)

def plan_task(plan_prompt: str):
    decision_prompt = f"""
    You are a Planner agent. Extract the required action and parameters from this request:
    "{plan_prompt}"

    Respond ONLY with a JSON object in this format:
    {{
        "action": "one of [list_resumes, count_files, fetch_file, none]",
        "params": {{
            "path": "the folder or file path if mentioned, else null",
            "extension": "the file extension if mentioned, else null"
        }}
    }}
    """
    
    response = llm.invoke(decision_prompt).content
    
    # Bug Fix: Use Regex to find the JSON block in case the LLM adds chatter
    try:
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            plan = json.loads(json_match.group())
        else:
            plan = json.loads(response) # Fallback
        return plan
    except Exception as e:
        print(f"Failed to parse JSON. Raw response: {response}")
        return {"action": "none", "params": {}}
