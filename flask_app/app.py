from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for demonstration purposes
users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('id')
    name = data.get('name')

    if not user_id or not name:
        return jsonify({'error': 'User ID and name are required'}), 400

    if user_id in users:
        return jsonify({'error': 'User ID already exists'}), 400

    users[user_id] = {'id': user_id, 'name': name}
    return jsonify({'message': 'User created successfully', 'user': users[user_id]}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'user': user}), 200

if __name__ == '__main__':
    app.run(debug=True)