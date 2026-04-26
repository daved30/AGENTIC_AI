import planner
import executor
import summarizer
from pprint import pformat

def ppfy(obj):
    return pformat(obj)

if __name__ == "__main__":
    print("--- Agentic System Started ---")
    user_prompt = input("What can I help you with? ")

    # 1. Planner
    try:
        plan = planner.plan_task(user_prompt)
        print(f"\n[Planner] Action: {plan.get('action')}")
    except Exception as e:
        print(f"Planner Error: {e}")
        plan = {"action": "none"}

    # 2. Executor
    print("[Executor] Running tool...")
    exec_output = executor.executor_agent(plan)
    print(f"[Executor] Result: {exec_output['final_output']}")

    # 3. Summarizer
    print("[Summarizer] Compiling final answer...")
    final_summary = summarizer.summarizer_agent([exec_output])
    
    print("\n" + "="*30)
    print("FINAL ANSWER:")
    print(final_summary)
    print("="*30)
