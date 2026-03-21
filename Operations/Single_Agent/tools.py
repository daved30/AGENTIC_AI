import os

def list_resumes(path=r"C:\\Users\\xyz\\Downloads"):
    """Return all files with 'resume' in the name."""
    return [f for f in os.listdir(path) if "resume" in f.lower()]

def count_files(path="C:/Users/xyz/Downloads", extension=".txt"):
    """Count files with a given extension."""
    return len([f for f in os.listdir(path) if f.endswith(extension)])

def fetch_file(path):
    """Read and return the contents of a file."""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return f"File not found: {path}"