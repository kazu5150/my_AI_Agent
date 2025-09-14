from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class Recipe(BaseModel):
    name: str
    servings: int
    ingredients: list[str]
    steps: list[str]

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "1人前のペスカトーレのレシピを教えてください。"}],
    temperature=0,
    response_format=Recipe,
)

recipe = response.choices[0].message.parsed
print(recipe.name)
print(f"Servings: {recipe.servings}")
print("Ingredients:")
for ingredient in recipe.ingredients:
    print(f"- {ingredient}")
print("Steps:")
for i, step in enumerate(recipe.steps, start=1):
    print(f"{i}. {step}")
print(f"Tokens used: {response.usage.total_tokens}")



