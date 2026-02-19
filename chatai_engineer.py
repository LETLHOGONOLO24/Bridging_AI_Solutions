import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key (I recommend renaming your .env variable to GEMINI_API_KEY for clarity)
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key loads
if not api_key:
    raise ValueError('API key not found. Please set GEMINI_API_KEY in your .env file.')

# Configure the Gemini client
genai.configure(api_key=api_key)

# Initialize the model (choose a free-tier model like 'gemini-2.0-flash' or 'gemini-2.5-flash')
model = genai.GenerativeModel('gemini-2.5-flash')

# Your prompt
prompt = "Explain object-oriented programming in Python."

# Generate the response
response = model.generate_content(prompt)

# Print the result
print(response.text)