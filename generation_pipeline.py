
from transformers import pipeline

gpt2_pipeline = pipeline(task="text-generation", model="openai-community/gpt2")

results = gpt2_pipeline(
    "The future of technology",
    max_new_tokens=10,
    num_return_sequences=2
)

# Print each generated result
for result in results:
    print(result['generated_text'])
    print("-" * 50)