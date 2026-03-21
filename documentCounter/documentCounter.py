import os
from langchain_community.chat_models import ChatOllama

ollama_model = os.getenv("OLLAMA_MODEL_NAME", "mistral")
llm = ChatOllama(model=ollama_model)

print("Model:", ollama_model)

def list_resumes(path=r"C:\\Users\\xyz\\Downloads"):
    resumes = [f for f in os.listdir(path) if 'resume' in f.lower()]
    return resumes

def agent(prompt):
    response = llm.invoke(prompt)
    print('LLM says: ', response)
    
    if 'resumes' in prompt.lower():
        files = list_resumes()
        print("Local Action: found resumes -> ", files)
        
agent("How many resume files do I have in Explorer?")