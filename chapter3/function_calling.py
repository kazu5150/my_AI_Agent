import json
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI()

# 天気予報を取得する関数（OpenWeatherMap API使用）
def get_weather(location):
    api_key = os.getenv('OPENWEATHER_API_KEY')

    if not api_key or api_key == "your_openweather_api_key_here":
        return f"OpenWeatherMap API keyが設定されていません。.envファイルでOPENWEATHER_API_KEYを設定してください。"

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # APIリクエストのパラメータ
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",  # 摂氏温度
        "lang": "ja"       # 日本語
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 404:
            return f"'{location}'が見つかりませんでした。より具体的な地名を試してください。例: 那覇市、沖縄市、石垣市など"

        response.raise_for_status()

        data = response.json()

        # 天気情報を整理
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        weather_report = f"{location}の天気: {weather_description}, 気温: {temperature}°C (体感温度: {feels_like}°C), 湿度: {humidity}%"

        return weather_report

    except requests.exceptions.RequestException as e:
        return f"天気情報の取得中にエラーが発生しました: {str(e)}"
    except KeyError as e:
        return f"天気データの解析中にエラーが発生しました: {str(e)}"
    except Exception as e:
        return f"予期しないエラーが発生しました: {str(e)}"

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
  
