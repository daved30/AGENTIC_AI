from langchain_community.chat_models import ChatOllama
import tools, json, os

print("|| Executor Agent ||")

ollama_model = os.getenv("OLLAMA_MODEL_NAME", "llama3.1:8b")
llm = ChatOllama(model=ollama_model, temperature=0)

def executor_agent(plan: dict):
    action = plan.get("action")
    raw_params = plan.get("params", {})

    # Clean up params: Remove nulls/none
    params = {k: v for k, v in raw_params.items() if v and v != "null"}

    # Step 1: Execute the tool (with parameter filtering)
    if action == "list_resumes":
        # list_resumes only takes 'path'
        tool_params = {k: v for k, v in params.items() if k == "path"}
        result = tools.list_resumes(**tool_params)
        
    elif action == "count_files":
        # count_files takes 'path' and 'extension'
        tool_params = {k: v for k, v in params.items() if k in ["path", "extension"]}
        result = tools.count_files(**tool_params)
        
    elif action == "fetch_file":
        # fetch_file only takes 'path'
        tool_params = {k: v for k, v in params.items() if k == "path"}
        result = tools.fetch_file(**tool_params)

    else:
        result = "I couldn't find a valid action to perform."

    # Step 2: Single clear explanation
    # We skip the "reasoning" step to avoid the long-winded double talk
    summary_prompt = f"""
    You are an Executor Agent. 
    Task: {action}
    Result from tool: {result}
    
    Provide a one-sentence, direct answer to the user. Do not explain your process.
    """
    final = llm.invoke(summary_prompt).content
    
    return {
        "plan": plan,
        "raw_result": result,
        "final_output": final.strip()
    }