from langchain_community.chat_models import ChatOllama
import json, os

print("|| Summarizer Agent ||")

ollama_model = os.getenv("OLLAMA_MODEL_NAME", "mistral")
llm = ChatOllama(model=ollama_model)

print("Model:", ollama_model)

def summarizer_agent(executor_outputs: list):
    combined = "\n".join([json.dumps(o, indent=2) for o in executor_outputs])
    prompt = f"""
    You are a Summarizer agent.
    Here are the results from other agents:
    {combined}

    Summarize them into a clear, concise final answer for the user.
    """
    return llm.invoke(prompt).content
