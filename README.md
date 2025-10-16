# Semantic Kernel Azure OpenAI Chat

This project is a Python console application using Semantic Kernel to chat with an Azure OpenAI GPT-5 model. It integrates an OpenAPI spec as a tool for the model. The system prompt is stored in `system_prompt.md` for easy editing.

## Features

- Console chat with Azure OpenAI GPT-5
- OpenAPI tool integration via `weather_openapi.json`
- Editable system prompt

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Rename or copy `.env.sample` to `.env`, then edit the file and fill in your actual Azure OpenAI credentials. The application expects:

   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_KEY`
   - `AZURE_OPENAI_DEPLOYMENT`

## Usage

Run the chat application:

```pwsh
python main.py
```

Edit `system_prompt.md` to change the system prompt.

## OpenAPI Spec

The project uses `weather_openapi.json` (wttr.in) as the default tool specification. Replace this file to use a different API.
