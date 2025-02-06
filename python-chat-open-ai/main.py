
from fastapi import FastAPI
from pydantic import BaseModel
import os
import aiohttp

app = FastAPI()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


# Set your OpenAI API key
# openai.api_key = OPENAI_API_KEY

class Query(BaseModel):
    prompt: str

@app.post("/generate/")
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
            return {"response": data['choices'][0]['message']['content'].strip()}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI and OpenAI Integration!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

# @app.get("/")
# async def default():
#     return "Fast API - with GPT-4 integration!"

# async def chat_with_gpt(prompt):
#     async with aiohttp.ClientSession() as session:
#         response = await session.post(
#             'https://api.openai.com/v1/chat/completions',
#             headers={
#                 'Authorization': f'Bearer {OPENAI_API_KEY}',
#                 'Content-Type': 'application/json'
#             },
#             json={
#                 'model': 'gpt-4',
#                 'messages': [
#                     {'role': 'system', 'content': 'You are a helpful assistant!'},
#                     {'role': 'user', 'content': prompt}
#                 ]
#             }
#         )
#         data = await response.json()
#         return data['choices'][0]['message']['content'].strip("\n").strip()

# @app.post("/chat")
# async def chat_gpt(user_input:UserInput):
#     try:
#         user_input.response = await chat_with_gpt(user_input.prompt)
#         return user_input
#     except Exception as e:
#         error_message = str(e)
#         return {"error": "Chat failed", "details": error_message}  


