import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(location):
    """OpenWeatherMap APIを使用して天気情報を取得するテスト関数"""
    api_key = os.getenv('OPENWEATHER_API_KEY')

    if not api_key or api_key == "your_openweather_api_key_here":
        return "OpenWeatherMap API keyが設定されていません。.envファイルでOPENWEATHER_API_KEYを設定してください。"

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",
        "lang": "ja"
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 404:
            return f"'{location}'が見つかりませんでした。より具体的な地名を試してください。\n例: 那覇市、沖縄市、石垣市など"

        response.raise_for_status()

        data = response.json()

        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        weather_report = f"{location}の天気: {weather_description}, 気温: {temperature}°C (体感温度: {feels_like}°C), 湿度: {humidity}%"

        return weather_report

    except requests.exceptions.RequestException as e:
        return f"天気情報の取得中にエラーが発生しました: {str(e)}"
    except Exception as e:
        return f"予期しないエラーが発生しました: {str(e)}"

if __name__ == "__main__":
    # ユーザーからの入力を受け取る
    location_input = input("天気を知りたい場所を入力してください: ")

    result = get_weather(location_input)
    print(result)