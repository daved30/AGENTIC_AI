import os

# This helper finds the "Home" folder automatically (e.g., /Users/dave on Mac)
HOME = os.path.expanduser("~")
DEFAULT_PATH = os.path.join(HOME, "Documents")

def list_resumes(path=DEFAULT_PATH):
    try:
        return [f for f in os.listdir(path) if "resume" in f.lower()]
    except Exception as e:
        return f"Error accessing path: {e}"

def count_files(path=DEFAULT_PATH, extension=".txt"):
    try:
        return len([f for f in os.listdir(path) if f.endswith(extension)])
    except Exception as e:
        return f"Error: {e}"

def fetch_file(path=None):
    # If no path provided, look for a test.txt in Documents
    if path is None:
        path = os.path.join(DEFAULT_PATH, "test.txt")
    
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        return f"File not found at: {path}"
    except Exception as e:
        return f"Could not read file: {e}"
