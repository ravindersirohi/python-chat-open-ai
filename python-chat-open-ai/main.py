
from fastapi import FastAPI
from pydantic import BaseModel
import os
import aiohttp

app = FastAPI()

# Set your OpenAI API key - Refer readme file.
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

class Query(BaseModel):
    prompt: str
    response: str = None

@app.post("/generate")
async def generate_text(query: Query):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {OPENAI_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'gpt-4',
                'messages': [{'role': 'user', 'content': query.prompt}]
            }
        ) as response:
            data = await response.json()
            query.response = data['choices'][0]['message']['content'].strip('\n').strip()
            return query

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI and OpenAI Integration!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))  


