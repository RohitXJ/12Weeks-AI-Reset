import os
from openai import OpenAI

# 1. Initialize the local client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',
)

# 2. Function to read all text files in your 'my_docs' folder
def load_local_data(folder_path):
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                all_text += f"\n--- Source: {filename} ---\n{f.read()}\n"
    return all_text

def run_agent():
    # Load your local "knowledge base"
    knowledge = load_local_data(r"Side_Quest\Adventure_1\my_docs")
    
    if not knowledge:
        print("⚠️ No .txt files found in ./my_docs. Add some and try again!")
        return

    print("🧠 Local Agent is ready. Ask anything about your files (Type 'exit' to quit).")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit': break

        # The "Extraordinary" part: Injecting local data into the prompt
        response = client.chat.completions.create(
            model="llama3.2",
            messages=[
                {
                    "role": "system", 
                    "content": f"You are a local assistant. Use this data to answer: {knowledge}"
                },
                {"role": "user", "content": user_input}
            ]
        )
        
        print(f"\n🤖 Agent: {response.choices[0].message.content}")

if __name__ == "__main__":
    run_agent()