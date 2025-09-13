from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    response_format={"type": "json_object"},
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": " あなたはJSONを出力するように設計された便利なアシスタントです。"},
        {"role": "assistant", "content": "JSONの形式は以下のとおりです。"},
        {"role": "assistant", "content": "```json"},
        {"role": "assistant", "content": "{"},
        {"role": "assistant", "content": "  \"title\": \"ロバートAハインラインの「夏への扉」という小説はなぜ日本で人気なのですか？\""},
        {"role": "assistant", "content": "}"},
        {"role": "assistant", "content": "```"},
        {"role": "user", "content": "ロバートAハインラインの「夏への扉」という小説はなぜ日本で人気なのですか？"}],
)

print(response.choices[0].message.content)
