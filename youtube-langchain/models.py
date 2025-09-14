from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv


load_dotenv()
message = HumanMessage(content="自己紹介してください。")


model = ChatOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    model="gpt-4o-mini",
    temperature=1
)

response = model.invoke([message])
print(response.content)
