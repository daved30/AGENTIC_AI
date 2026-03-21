import os

def list_resumes(path="C:/Users/xyz/Downloads"):
    return [f for f in os.listdir(path) if "resume" in f.lower()]

def count_files(path="C:/Users/xyz/Downloads", extension=".pdf"):
    return len([f for f in os.listdir(path) if f.endswith(extension)])

def fetch_file(path="C:/Users/xyz/Downloads/test.pdf"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return f"File not found: {path}"