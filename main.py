import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions

parser = argparse.ArgumentParser(description="Agent")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action = "store_true", help="Enable verbose output")
args = parser.parse_args()

def main():

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key == None:
        raise RuntimeError("No OpenRouter API key found")

    client = OpenAI(
            base_url = "https://openrouter.ai/api/v1",
            api_key = api_key
    )

    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": args.user_prompt}
    ]

    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = messages,
        tools = available_functions,
    )

    message = response.choices[0].message

    if response.usage == None:
        raise RuntimeError("API request failed")

    if args.verbose == True:
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        print(f"User prompt: {args.user_prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {completion_tokens}")

    if message.tool_calls != None:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling functions: {tool_call.function.name}({function_args})")
    else:
        print(f"Response:\n{response.choices[0].message.content}")

if __name__ == "__main__":
    main()
