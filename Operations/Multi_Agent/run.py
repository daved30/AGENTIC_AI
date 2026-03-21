import planner, executor
from pprint import pformat

def ppfy(obj):
    return pformat(obj)
    
import planner, executor, summarizer

if __name__ == "__main__":
    # user_prompt = "Fetch file C:/Users/xyz/Downloads/test.pdf and count resumes."
    user_prompt = input("Enter the prompt: ")

    # Planner decides
    plan = planner.plan_task(user_prompt)
    print(type(plan))
    print("Planner decided:", ppfy(plan))
    del planner

    # Executor runs
    exec_output = executor.executor_agent(plan)
    print(type(exec_output))
    print("Executor output:", ppfy(exec_output["final_output"]))
    del executor

    # Summarizer compiles
    summary = summarizer.summarizer_agent([exec_output])
    print(type(summary))
    print("Summarizer says:", ppfy(summary))
    del summarizer