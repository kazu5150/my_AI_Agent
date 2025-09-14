import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


model = ChatOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    model="gpt-4o",
    temperature=0
)
output = model.invoke("自己紹介してください。")
print(output)
