import json

def log_response(resp):
    """
    Pretty-print the LLM response object in a clean format.
    """
    # Extract main fields
    content = getattr(resp, "content", None) or resp.get("content", "")
    metadata = getattr(resp, "response_metadata", None) or resp.get("response_metadata", {})
    run_id = getattr(resp, "id", None) or resp.get("id", "")

    print("\n=== AGENT OUTPUT ===")
    print(f"Run ID: {run_id}")
    print(f"Model: {metadata.get('model', 'unknown')}")
    print(f"Created At: {metadata.get('created_at', 'unknown')}")
    print("\n--- Content ---")
    print(content.strip() if content else "[No content]")
    print("\n--- Metadata ---")
    print(json.dumps(metadata, indent=4))
    print("====================\n")
