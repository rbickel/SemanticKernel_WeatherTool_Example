# Semantic Kernel Azure OpenAI Chat

This project is a Python console application using Semantic Kernel to chat with an Azure OpenAI GPT-5 Codex model. It integrates an OpenAPI spec as a tool for the model. The system prompt is stored in `system_prompt.md` for easy editing.

## Features

- Console chat with Azure OpenAI GPT-5 Codex
- OpenAPI tool integration via `weather_openapi.json`
- Editable system prompt

## Setup

1. Create and activate a virtual environment (recommended):

   ```pwsh
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```pwsh
   pip install -r requirements.txt
   ```

3. Set your Azure OpenAI endpoint and key in environment variables or a `.env` file:

   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_KEY`
   - `AZURE_OPENAI_DEPLOYMENT` (GPT-5 Codex deployment name)

## Usage

Run the chat application:

```pwsh
python main.py
```

Edit `system_prompt.md` to change the system prompt.

## OpenAPI Spec

The project uses `weather_openapi.json` (wttr.in) as the default tool specification. Replace this file to use a different API.
