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
        temperature=temperature,
        max_tokens=500
    )
    return response.choices[0].message.content

# Create a detailed prompt for better results
prompt = """Please generate a table of 10 science fiction books that every sci-fi lover should read.

Requirements:
- Format the response as a markdown table
- Include exactly 3 columns: Title, Author, and Year
- List 10 different books
- Include a mix of classics and contemporary works
- Sort by Year (oldest to newest)

The table should look like this format:
| Title | Author | Year |
|-------|--------|------|
| Book 1 | Author 1 | Year 1 |
| Book 2 | Author 2 | Year 2 |"""

# Get and display the response
response = get_response(prompt)
print("=== MUST-READ SCIENCE FICTION BOOKS ===\n")
print(response)