from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database / MongoDB connection configuration
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',  # Replace with your MySQL username
    'password': 'password',  # Replace with your MySQL password
    'database': 'example_db'  # Replace with your database name
}

# In-memory database for demonstration purposes
users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # print(data)
    user_id = data.get('id')
    name = data.get('name')

    if not user_id or not name:
        return jsonify({'error': 'User ID and name are required'}), 400

    if user_id in users:
        return jsonify({'error': 'User ID already exists'}), 400
    
    # Insert user into MySQL database
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO example_db.users (id, name) VALUES (%s, %s)", (user_id, name))
        connection.commit()
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500

    users[user_id] = {'id': user_id, 'name': name}
    return jsonify({'message': 'User created successfully', 'user': users[user_id]}), 201
@app.route('/users', methods=['GET'])
def get_user():
    # using header
    # user_id = request.headers.get('id')
    # name = request.headers.get('user')
    # using query parameter
    user_id = request.args.get('id')
    name = request.args.get('user')

    if user_id:
        user = users.get(user_id)
        if user:
            return jsonify({'user': user}), 200
        return jsonify({'error': 'User not found'}), 404

    if name:
        for user in users.values():
            if user['name'] == name:
                return jsonify({'user': user}), 200
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'error': 'Either id or user header is required'}), 400

@app.route('/users', methods=['DELETE'])
def delete_user():
    # using header
    # user_id = request.headers.get('id')
    # name = request.headers.get('user')
    # using query parameter
    user_id = request.args.get('id')
    name = request.args.get('user')

    if user_id:
        if user_id in users:
            deleted_user = users.pop(user_id)
            return jsonify({'message': 'User deleted', 'user':deleted_user}), 200
        return jsonify({'error': 'User not found'}), 404

    if name:
        user_to_delete = None
        for key, user in list(users.items()):
        # convert to list to avoid runtime errors during deletion
            if user['name'] == name:
                user_to_delete = key
                break
        
        if user_to_delete:
            deleted_user = users.pop(user_to_delete)
            return jsonify({'message': 'User deleted', 'user': deleted_user}), 200
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'error': 'Either id or user header is required'}), 400

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    new_name = data.get('name')

    if not new_name:
        return jsonify({'error': 'New name is required'}), 400

    users[user_id]['name'] = new_name
    return jsonify({'message': 'User updated', 'user': users[user_id]}), 200

if __name__ == '__main__':
    app.run(debug=True)