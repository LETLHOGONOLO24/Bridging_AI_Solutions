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
        max_tokens=100
    )
    return response.choices[0].message.content

ticket = """Hello Support Team,

I was charged twice for my subscription this month, but I can only see one active plan in my account dashboard.
I've already checked my payment history and bank statement, and the duplicate charge is still showing. Could you
please look into this and help resolve the issue as soon as possible?

Thank you.
"""

prompt = f"""
You are a ticket classification system for a customer support team. Your task is to analyze the customer ticket
below and classify it into exactly one of three categories: "technical issue", "billing inquiry", or "product feedback".

Classification guidelines:
- "technical issue": Problems with product functionality, errors, bugs, system crashes, features not working,
login problems, performance issues, or any technical malfunction
- "billing inquiry": Questions about charges, invoices, payments, subscriptions, refunds, pricing, discounts, or any financial transactions
- "product feedback": Suggestions for improvements, feature requests, general opinions about the product,
compliments, or complaints about product design/usability

Return ONLY the category name in lowercase. Do not include any explanations, introductions, or additional text.

```{ticket}```
"""

response = get_response(prompt)
print("=== Text Analysis ===\n")
print(response)