# Adventure 2: The Local Ghost 👻

This document details the project codenamed "The Local Ghost," an experiment to create a 100% private, locally-hosted AI coding assistant in VS Code, completely replacing cloud-based services like GitHub Copilot.

## The Goal
The primary objective was to run a local AI coding agent on a personal machine (RTX 3050) using Ollama and the Continue extension for VS Code. The chosen model was `Qwen 2.5 Coder` to handle chat, refactoring, and autocompletion without sending any code to external servers.

## The Problems Encountered
The journey wasn't straightforward. Several critical issues emerged:

1.  **Pathing & Storage:** Ollama defaulted its model storage to the main `C:` drive, risking filling up critical system space.
2.  **Visibility Issues:** Models were downloaded to one directory while the Ollama server was looking in another, making them "invisible" to the `ollama list` command.
3.  **The "EOF" Error:** VS Code's Continue extension failed to connect to the local model, repeatedly throwing a generic "End of File" (EOF) error.
4.  **Bad Manifest Error:** Digging into the logs revealed a `bad manifest config` error, pointing to corrupted model metadata from an interrupted download.

## The Engineering Steps to Fix It
A systematic approach was taken to diagnose and resolve the issues:

1.  **System Realignment:** Identified and terminated multiple "zombie" `ollama.exe` processes that were holding onto old, incorrect configurations.
2.  **Infrastructure Setup:**
    *   Created a dedicated directory for AI models on a separate `F:` drive (`F:\Ollama\models`).
    *   Set the Windows System Environment Variable `OLLAMA_MODELS` to this new path, forcing Ollama to use the correct storage location.
3.  **Corrupted Data Purge:**
    *   Manually deleted the corrupted `qwen2.5-coder` manifest folder to resolve the "Bad Manifest" error.
    *   Used `ollama rm` to completely unregister the broken model from the system.
4.  **Environment Bridge:**
    *   Configured the `config.yaml` file within the Continue extension to explicitly map the `chat` and `autocomplete` roles to the locally-run models.

## The Final Stack
The successful local setup consists of:

-   **Host:** Windows 11 / RTX 3050 (4GB/8GB VRAM) / 16GB RAM
-   **Backend:** Ollama (serving models from the `F:` Drive)
-   **Primary Coder Model:** `qwen2.5-coder:3b` (Fast, logical, and fits within VRAM)
-   **Autocomplete Model:** `qwen2.5-coder:1.5b` (For instant suggestions)
-   **IDE:** VS Code with the **Continue** Extension

## Conclusion
Stability was achieved by forcing the Ollama server and the system's terminal environment to align on the same model directory and by purging corrupted metadata. The "EOF" error was ultimately a symptom of the server's inability to find a healthy, properly located model file. The result is a fast, private, and effective local AI coding assistant.
