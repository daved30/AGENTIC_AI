from langchain_community.chat_models import ChatOllama
import json
import os

print("|| Planner Agent ||")

ollama_model = os.getenv("OLLAMA_MODEL_NAME", "mistral")
llm = ChatOllama(model=ollama_model)

print("Model:", ollama_model)

def plan_task(plan_prompt: str):
    decision_prompt = f"""
    You are a Planner agent. Decide what tool to use for this request:
    "{plan_prompt}"

    Remember to Respond in only JSON with:
    - action: one of [list_resumes, count_files, fetch_file, none]
    and nothing else only the required action taken.
    """
    response = llm.invoke(decision_prompt).content
    print(response)

    plan = json.loads(response)

    return plan
