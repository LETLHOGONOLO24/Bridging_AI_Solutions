import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create client
client = OpenAI()

developer_message = 'You are a concise assistant. You reply briefly with no elaboration'

try:
    response = client.responses.create(
        model='gpt-4o-mini',  # Try this model first
        input = [
            {'role': 'developer', 'content': developer_message},
            {'role': 'user', 'content': 'Explain Object_Oriented Programming with Python.'}
        ]
    )
    
    print(response.output_text)
    print('=========================================')
    print(response.choices[0].message.content)
    
except Exception as e:
    print(f"An error occurred: {e}")