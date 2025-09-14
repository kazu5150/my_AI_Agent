from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(model="gpt-3.5-turbo")
template = ChatPromptTemplate.from_messages([
    ("system", "あなたはいつもふざけて笑わせてくれる面白いアシスタントです。"), 
    ("user", "{question}")
])

chain = template | llm
response = chain.invoke({"question": "おもしろい冗談を言ってください"})
print(response.content)
