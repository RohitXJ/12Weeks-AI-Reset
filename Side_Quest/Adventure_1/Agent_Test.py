from openai import OpenAI

# Connect to your LOCAL Ollama server
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama', # Ollama doesn't need a real key, but the library requires one
)

response = client.chat.completions.create(
  model="llama3.2",
  messages=[
    {"role": "system", "content": "You are a helpful AI Engineer assistant."},
    {"role": "user", "content": "Hello! Confirm you are running locally on my machine."}
  ]
)

print(response.choices[0].message.content)