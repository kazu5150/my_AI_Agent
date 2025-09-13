import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": "ロバートAハインラインの「夏への扉」という小説はなぜ日本で人気なのですか？"
    }],
)

print(response.choices[0].message.content)
print(f"Tokens used: {response.usage.total_tokens}")