import ollama
response = ollama.chat(
    model="mistral",
    messages=[{'role': "user",
               'content': "Hello, Local LLM, are you working and if yes what is your name?"}]
)

print(response['message']['content'])