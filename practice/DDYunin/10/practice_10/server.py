from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

_url = 'https://jsonplaceholder.typicode.com/users/{0}'

@app.get('/users/{user_id:int}')
async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(_url.format(user_id))
    return r.json()


@app.get('/')
async def read_root():
     return {"Hello": "World"}
