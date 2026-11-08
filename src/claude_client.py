import os
import anthropic
from dotenv import load_dotenv

# 1. Load the .env file into environment variables
load_dotenv()

# 2. Read the API key (never written in the code)
api_key = os.getenv("ANTHROPIC_API_KEY")

# 3. Stop with a clear message if the key is missing
if not api_key:
    print("Error: ANTHROPIC_API_KEY not found. Add it to your .env file.")
    raise SystemExit(1)

client = anthropic.Anthropic(api_key=api_key)


# 4. Send any prompt to Claude and return the text answer
def ask_claude(prompt):
    try:
        message = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        )
        for block in message.content:
            if block.type == "text":
                return block.text
        return None
    except anthropic.APIError as error:
        print(f"Error: the Claude API call failed. Details: {error}")
        return None


if __name__ == "__main__":
    print(ask_claude("In one sentence, greet the COO of a commercial real estate company."))