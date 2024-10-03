import requests
import asyncio
import websockets
import json

async def connect_to_server():
    token = my_token  # Генерация уникального токена
    ip = "127.0.0.1"  # Пример IP адреса клиента
    port = 12345  # Пример порта клиента

    async with websockets.connect("ws://localhost:7890") as websocket:
        # Формирование данных для отправки
        data = {
            'token': token,
            'ip': ip,
            'port': port
        }

        # Отправка данных на сервер
        await websocket.send(json.dumps(data))

        # Ожидание ответа от сервера
        response = await websocket.recv()
        print(response)

# Получение токена
response = requests.post('http://localhost:8080/login', json={'username': 'user', 'password': 'pass'})
token = response.json().get('token')

my_token = token
print(my_token)

# Запуск клиента
if __name__ == '__main__':
    asyncio.run(connect_to_server())