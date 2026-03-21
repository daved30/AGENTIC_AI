from langchain_community.chat_models import ChatOllama
import tools, json, os

print("|| Executor Agent ||")

ollama_model = os.getenv("OLLAMA_MODEL_NAME", "mistral")
llm = ChatOllama(model=ollama_model)

print("Model:", ollama_model)

def executor_agent(plan: dict):
    # Step 1: Reason about the plan
    reasoning_prompt = f"""
    You are an Executor agent. Here is the plan:
    {json.dumps(plan)}

    Decide how to run the tool and explain the result clearly.
    """
    reasoning = llm.invoke(reasoning_prompt).content

    # Step 2: Run the tool
    action = plan.get("action")
    params = plan.get("params", {})
    if action == "list_resumes":
        result = tools.list_resumes(**params)
    elif action == "count_files":
        result = tools.count_files(**params)
    elif action == "fetch_file":
        result = tools.fetch_file(**params)
    else:
        result = "No valid action."

    # Step 3: Wrap result with LLM
    summary_prompt = f"""
    Tool result: {result}
    Write a clear explanation for the user.
    """
    final = llm.invoke(summary_prompt).content

    return {
        "plan": plan,
        "executor_reasoning": reasoning,
        "raw_result": result,
        "final_output": final
    }
