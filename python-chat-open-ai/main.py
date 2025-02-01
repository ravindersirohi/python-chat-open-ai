
import openai, asyncio, os, aiohttp
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    prompt: str
    response: str = None

openai.api_key = os.getenv("OPENAI_API_KEY")

async def chat_with_gpt(prompt):
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {openai.api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'gpt-4',
                'messages': [
                    {'role': 'system', 'content': 'You are a helpful assistant!'},
                    {'role': 'user', 'content': prompt}
                ]
            }
        )
        data = await response.json()
        return data['choices'][0]['message']['content'].strip("\n").strip()

@app.get("/")
def main():
    return "Fast API - with GPT-4 integration!"

@app.post("/chat")
async def chat(user_input:UserInput):
    try:
        user_input.response = await chat_with_gpt(user_input.prompt)
        return user_input
    except Exception as e:
        error_message = str(e)
        return {"error": "Chat failed", "details": error_message}  

if __name__ == "__main__":
    asyncio.run(main())

