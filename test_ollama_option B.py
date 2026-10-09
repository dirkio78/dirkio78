import time
import ollama

STREAM_DELAY_SECONDS = 0.01

user_prompt= input('Enter your request: ')

stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': user_prompt}],
    stream=True,
)

for chunk in stream:
    content = chunk['message']['content']
    print(content, end='', flush=True)
    time.sleep(STREAM_DELAY_SECONDS)
print()
