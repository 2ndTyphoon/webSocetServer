import requests
import asyncio
import websockets
import json

async def hello():
    uri = "ws://localhost:7890"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(f"Response from server: {response}")

# Получение токена
response = requests.post('http://localhost:8080/login', json={'username': 'user', 'password': 'pass'})
token = response.json().get('token')

my_token = token
print(my_token)


if __name__ == "__main__":
    asyncio.run(hello())