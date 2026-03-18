import os
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_random_exponential
from openai import OpenAI

load_dotenv()

# Create an OpenAI API client
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# Add the appropriate parameters to the decorator
@retry(wait=wait_random_exponential(min=5, max=40), stop=stop_after_attempt(4))
def get_response(model, message):
    response = client.chat.completions.create(
        model=model,
        messages=[message]
    )
    return response.choices[0].message.content

# Test the function
print(get_response("gpt-4o-mini", {"role": "user", "content": "List ten holiday destinations."}))