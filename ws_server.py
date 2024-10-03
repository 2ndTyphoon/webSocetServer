import asyncio
import json
import websockets

async def ws_server(websocket):
    print("WebSocket: Server Started.")

    try:
        while True:
            name = await websocket.recv()
            age = await websocket.recv()

            if name == "" or age == "":
                print("Error Receiving Value from Client.")
                break

            print("Details Received from Client:")
            print(f"Name: {name}")
            print(f"Age: {age}")

            await websocket.send(f"Connected, {name}.")

    except websockets.ConnectionClosedError:
        print("Internal Server Error.")

async def main():
    async with websockets.serve(ws_server, "localhost", 7890):
        await asyncio.Future()  # run forever


# Словарь для хранения подключенных клиентов
connected_clients = {}

async def handler(websocket, path):

    # Ожидание получения данных от клиента
    message = await websocket.recv()
    data = json.loads(message)

    token = data['token']
    ip = data['ip']
    port = data['port']

async def check_clients():
    while True:
        # Здесь можно реализовать логику проверки состояния клиентов
        print(f"Connected clients: {len(connected_clients)}")
        await asyncio.sleep(10)  # Проверяем каждые 10 секунд

start_server = websockets.serve(handler, "localhost", 7890)

asyncio.get_event_loop().run_until_complete(start_server)
print("Server started on ws://localhost:7890")
asyncio.get_event_loop().run_forever()


# Хранение активных токенов и клиентов
active_tokens = {}


if __name__ == "__main__":
    asyncio.run(main())