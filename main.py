import os
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent
from rich.console import Console
from dotenv import load_dotenv
import asyncio

SYSTEM_PROMPT_PATH = "system_prompt.md"
OPENAPI_SPEC_PATH = "weather_openapi.json"

console = Console()

def load_system_prompt():
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read()

def load_openapi_spec():
    with open(OPENAPI_SPEC_PATH, "r", encoding="utf-8") as f:
        return f.read()

async def main():
    
    load_dotenv()
    
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    key = os.getenv("AZURE_OPENAI_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not all([endpoint, key, deployment]):
        console.print("[red]Please set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, and AZURE_OPENAI_DEPLOYMENT environment variables.[/red]")
        return

    chat_completion_service = AzureChatCompletion(
            endpoint=endpoint,
            api_key=key,
            deployment_name=deployment,
    )

    kernel = Kernel()
    kernel.add_service(chat_completion_service)

    # Load OpenAPI tool defined in weather_openapi.json
    # openapi_tool = OpenAPITool.from_file(OPENAPI_SPEC_PATH)
    weather_plugin = kernel.add_plugin_from_openapi(
            plugin_name="WeatherPlugin",
            openapi_document_path=OPENAPI_SPEC_PATH
        )    
    kernel.add_plugin(weather_plugin)

    # Load system prompt
    system_prompt = load_system_prompt()
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(
            endpoint=endpoint,
            api_key=key,
            deployment_name=deployment,
        ),
        name="WeatherAgent",
        instructions=system_prompt,
        plugins=[weather_plugin]
    )
    print("✅ Created weather forecast agent with plugin")

    thread = None
    
    console.print("[bold green]Semantic Kernel Azure OpenAI Chat[/bold green]")
    console.print("Type 'exit' to quit.\n")
    while True:
        user_input = console.input("[bold blue]You:[/bold blue] ")
        if user_input.strip().lower() == "exit":
            break
        
        response = await agent.get_response(
            messages=user_input,
            thread=thread,
        )
        
        #chat_history.add_assistant_message(response)
        console.print(f"[bold magenta]Assistant:[/bold magenta] {response}")
        thread = response.thread

if __name__ == "__main__":
    asyncio.run(main())
