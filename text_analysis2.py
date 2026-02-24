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

# Sample tickets
ticket_1 = (
    "Hi Support Team, I’m unable to log into my account since yesterday. "
    "I keep getting an error message saying “authentication failed” even though my password "
    "is correct. My username is john.doe@email.com. Please help me fix this issue as soon as "
    "possible."
)

ticket_2 = (
    "Hello, I noticed that my credit card was charged twice for my monthly "
    "subscription on August 10, 2025. The amount charged was $49.99 each time. "
    "My order ID is ORD-45821. I’d appreciate it if you could check this and process a "
    "refund for the extra charge."
)

ticket_3 = (
    "Hey team, I just wanted to share some feedback about your new mobile app update. "
    "The interface looks much cleaner and the app feels faster, but the notification "
    "settings are a bit confusing to use. Overall, great work!"
)

ticket_4 = (
    "Good afternoon, my name is David Miller and I’m contacting you regarding a "
    "booking I made through your travel app. My reservation ID is TRV-90217 for a flight "
    "from New York to London scheduled on September 15, 2025. I need to update the passenger "
    "phone number linked to this booking. Please let me know how to proceed."
)

# Sample extracted entities
entities_1 = {
    "issue_type": "technical_issue",
    "problem": "authentication failed",
    "username": "john.doe@email.com"
}

entities_2 = {
    "issue_type": "billing_inquiry",
    "charge_amount": "$49.99",
    "charge_date": "August 10, 2025",
    "order_id": "ORD-45821",
    "request": "refund"
}

entities_3 = {
    "issue_type": "product_feedback",
    "product": "mobile app",
    "positive_feedback": ["cleaner interface", "faster performance"],
    "negative_feedback": ["confusing notification settings"]
}

# Craft a few-shot prompt
prompt = f"""
You are an entity extraction system for a customer support team. Your task is to extract key entities from customer support tickets.
Below are three examples of tickets with their extracted entities. Use these examples to understand what entities to look for
and how to format them. Then extract entities from the new ticket provided.

Example 1:
Ticket: "My premium subscription was charged $49.99 instead of $39.99 on March 15th. I need this corrected immediately.
My account email is john.doe@email.com."
Entities:
- Issue Type: billing error
- Amount: $49.99
- Expected Amount: $39.99
- Date: March 15th
- Account Email: john.doe@email.com
- Priority: high

Example 2:
Ticket: "The mobile app keeps crashing every time I try to upload a photo. I'm using version 2.1.3 on Android. This started
happening after the latest update."
Entities:
- Issue Type: technical bug
- Feature: photo upload
- Device: Android
- App Version: 2.1.3
- Trigger: after latest update
- Priority: medium

Example 3:
Ticket: "Can you add a dark mode to your application? Many users have been requesting this feature. It would really help
with eye strain during night use."
Entities:
- Issue Type: feature request
- Requested Feature: dark mode
- User Base: multiple users
- Benefit: reduce eye strain at night
- Priority: low

Now extract entities from this new ticket. Return ONLY the entities in the same format as the examples above, with each
entity on a new line starting with a hyphen and the entity name followed by a colon and the value. Do not include any
explanations or additional text.

sample 1:
{ticket_1}
entities:
{entities_1}

sample 2:
{ticket_2}
entities:
{entities_2}

sample 3:
{ticket_3}
entities:
{entities_3}

new ticket:
```{ticket_4}```
"""

response = get_response(prompt)

print("Ticket:\n", ticket_4)
print("Entities:\n", response)