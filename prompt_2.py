import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def get_response(prompt, temperature=0):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content

story = """Once upon a time, in a small village nestled between rolling hills, there lived a young
girl named Elara who discovered a mysterious glowing stone near the old oak tree. When she picked
it up, she felt a strange warmth spread through her fingers, and suddenly she could understand the
language of the birds singing above her."""

prompt = f"""Complete the story delimited by triple backticks. 
 ```{story}```"""

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)