from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser 


from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-4o",
    temperature=1
)

template = ChatPromptTemplate.from_messages([
    ("system", "あなたは、SF映画に詳しい料理アシスタントです。"), 
    ("user", "このテーマで作成されたSF映画を教えてください。テーマ：{theme}")
])

chain = template | llm | StrOutputParser()
response = chain.invoke({"theme": "タイムトラベル"})
print(response)
