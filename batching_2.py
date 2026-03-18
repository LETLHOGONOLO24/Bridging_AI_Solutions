import os
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_random_exponential
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

measurements = [5.0, 10.0, 21.1, 42.2, 100.0]

# Define the get_response function (with retry decorator)
@retry(wait=wait_random_exponential(min=5, max=40), stop=stop_after_attempt(4))
def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content

# Now your code from the exercise
messages = []
# Provide a system message
messages.append({
    "role": "system",
    "content": "Convert each measurement, given in kilometers, into miles, and reply with a table of all measurements."
})

# Append measurements as user messages
for measurement in measurements:
    messages.append({
        "role": "user",
        "content": str(measurement)
    })

# Get and print the response
response = get_response(messages)
print(response)