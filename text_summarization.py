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

product_description = """The smartphone features a 6.7-inch AMOLED display with a 120 Hz refresh rate, offering smooth visuals and vibrant colors.
It is poweredby a high-performance processor that ensures fast multitaskingand gaming. The device includes a 5000mAh battery that supports
fast charging, allowing extendedusage throughout the day. The smartphone comes with a triple-camera system, including a 64MP main camera, an
ultra-wide lens,and a macro sensor, delivering high-quality photo sand videos. It also offers 5G connectivity, enhanced security features such
as anin-display fingerprint sensor,and runson the latest versionof the operating system."""

prompt = f"""
Summarize the following smartphone product description in no more than five bullet points.
Highlight the key features that would help users quickly compare and evaluate the product.

Product Description:{product_description}
"""

response = get_response(prompt)
print("=== Product Description ===\n")
print(response)