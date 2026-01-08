# Adventure 1: Local LLM Interaction with Ollama

This adventure demonstrates how to set up and interact with a local Large Language Model (LLM) using Ollama and the `openai` Python library. We'll be using the `llama3.2` model.

## Prerequisites

Before running the scripts, ensure you have the following installed:

1.  **Ollama:** Download and install Ollama from [ollama.ai](https://ollama.ai/).
2.  **Llama3.2 Model:** Once Ollama is installed, open your terminal or command prompt and pull the `llama3.2` model:
    ```bash
    ollama pull llama3.2
    ```
3.  **Python Libraries:** Install the `openai` library (if you haven't already):
    ```bash
    pip install openai
    ```

## Files in this Adventure

### `Agent_Test.py`

This script provides a basic example of connecting to your local Ollama server and interacting with the `llama3.2` model. It acts as a simple "hello world" test to ensure your Ollama setup is working correctly.

**How it works:**
- It initializes an `OpenAI` client, pointing its `base_url` to the local Ollama server (`http://localhost:11434/v1`).
- It uses a dummy `api_key` as required by the library, even though Ollama doesn't use one for local access.
- It sends a system message and a user message to the `llama3.2` model and prints the model's response.

**To run:**
```bash
python Agent_Test.py
```

### `System_prompting.py`

This script demonstrates a more advanced use case: building a local agent that can answer questions based on a local "knowledge base" stored in text files within the `my_docs` folder.

**How it works:**
1.  **Client Initialization:** Similar to `Agent_Test.py`, it initializes an `OpenAI` client to connect to the local Ollama server.
2.  **`load_local_data(folder_path)`:** This function reads all `.txt` files from a specified folder (`my_docs` in this case) and concatenates their content into a single string. This aggregated text serves as the agent's knowledge base.
3.  **`run_agent()`:**
    *   Loads the content from `my_docs`.
    *   Enters a loop, prompting the user for input.
    *   For each user input, it constructs a `messages` list for the LLM. Crucially, it injects the entire `knowledge` string into the system prompt, instructing the model to use this data for its answers.
    *   Prints the agent's response.

**`my_docs` folder:**
This folder is intended to hold your local `.txt` files that the `System_prompting.py` script will use as its knowledge base. Currently, it contains `secret_plan.txt`.

**To run:**
```bash
python System_prompting.py
```
You can then type questions, and the agent will try to answer them based on the content of `secret_plan.txt` (or any other `.txt` files you add to `my_docs`). Type `exit` to quit.
