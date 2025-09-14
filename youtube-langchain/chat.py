from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


load_dotenv()
model = ChatOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    model="gpt-4o-mini",
    temperature=1
)


messages = [
    SystemMessage(content="こんにちは、私はAIのHARUと言います。2001年宇宙の旅に出てきたAIを同じ名前です。"),
    HumanMessage(content="私の名前はKazuと言います。"),
    AIMessage(content="Kazuさん、こんにちは！お会いできて嬉しいです。何かお手伝いできることはありますか？"),
    HumanMessage(content="私の名前を知っていますか？")
]


ai_message = model.invoke(messages)
print(ai_message.content)
