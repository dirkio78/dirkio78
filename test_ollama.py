import ollama

response = ollama.generate(
    model='llama3',
    prompt='Explain the Rustdesk app and how it works'
)

print(response['response'])