import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def get_response(prompt):
    """
    Function to get a response from OpenAI API
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that always responds with properly formatted tables."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
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