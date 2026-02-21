import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key (I recommend renaming your .env variable to GEMINI_API_KEY for clarity)
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key loads
if not api_key:
    raise ValueError('API key not found. Please set GEMINI_API_KEY in your .env file.')

client = OpenAI()

prompt = "____"
response = ____
print(response)
