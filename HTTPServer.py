from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Хранение токенов (в реальном приложении используйте базу данных)
active_tokens = {}


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Здесь должна быть ваша логика аутентификации
    if username == 'user' and password == 'pass':  # Пример проверки
        token = str(uuid.uuid4())
        active_tokens[token] = username  # Сохраняем токен и связанного пользователя

        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401


if __name__ == '__main__':
    app.run(port=8080)