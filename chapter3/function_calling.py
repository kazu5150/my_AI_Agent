import json
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI()

# 天気予報を取得するダミー関数
def get_weather(location):
    # 実際には、ここで天気予報APIを呼び出すコードが入ります
    weather_info = {
        "東京": "晴れ、最高気温25度",
        "大阪": "曇り、最高気温22度",
        "長野": "晴れ、最高気温20度"
    }
    return weather_info.get(location, "情報がありません")

# ユーザーからの入力を受け取る
location_input = input("天気を知りたい場所を入力してください: ")

# 初回のユーザーメッセージ
message = [{"role": "user", "content": f"明日の{location_input}の天気を教えてください。"}]

# モデルに提供するツールの定義
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "指定された場所の天気予報を取得します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "天気予報を取得したい場所の名前（例：東京、大阪、長野）"
                    }
                },
                "required": ["location"]
            }
        }
        
    }
]

# モデルへの最初のAPIリクエスト
response = client.chat.completions.create(
    model="gpt-4o",
    messages=message,
    tools=tools,
    tool_choice="auto"  # 自動的に関数を呼び出す
)
# モデルの応答を処理
response_message = response.choices[0].message
message.append(response_message)

# 関数呼び出しを処理
if response_message.tool_calls:
    for tool_call in response_message.tool_calls:
        if tool_call.function.name == "get_weather":
            # 関数の引数を取得
            function_args = json.loads(tool_call.function.arguments)
            print(f"関数の引数：{function_args}")
            weather_response = get_weather(
                location=function_args.get("location")
            )
            message.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": "get_weather",
                "content": weather_response
            })
else:
    print("関数呼び出しはありません。")
    

# モデルへの最終的なAPIリクエスト
final_response = client.chat.completions.create(
    model="gpt-4o",
    messages=message
)
print(f"最終応答：{final_response.choices[0].message.content}")
  
