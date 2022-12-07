from fastapi import FastAPI
import httpx

app = FastAPI()

_url = 'https://jsonplaceholder.typicode.com/users/'

@app.get('/users/{user_id:int}')
async def get_user(request, user_id: int):
     return await httpx.get(_url + str(id))

@app.get('/')
async def read_root():
     return await {"Hello": "World"}