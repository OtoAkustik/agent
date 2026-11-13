import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

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
            {"role": "user", "content": args.user_prompt}
    ]

    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = messages,
    )

    if response.usage == None:
        raise RuntimeError("API request failed")

    if args.verbose == True:
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        print(f"User prompt: {args.user_prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {completion_tokens}")

    print(f"Response:\n{response.choices[0].message.content}")

if __name__ == "__main__":
    main()
