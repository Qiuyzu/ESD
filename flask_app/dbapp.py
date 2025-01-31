from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'port': 8889,
    'user': 'root',
    'password': 'root',
    'database': 'example_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('id')
    name = data.get('name')

    if not user_id or not name:
        return jsonify({'error': 'User ID and name are required'}), 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (user_id, name))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'User created successfully', 'user': {'id': user_id, 'name': name}}), 201
    
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500

# get user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT id, name FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            return jsonify({'user': user}), 200
        return jsonify({'error': 'User not found'}), 404
    
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500
    
# delete user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        if not user:
            cursor.close()
            conn.close()
            return jsonify({'errror': 'User not found'}), 404
        
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'User deleted successfully'}), 200
    
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500
    
# update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        data = request.get_json()
        new_name = data.get('name')

        if not new_name:
            return jsonify({'error': 'New name is required'}), 400
        
        cursor.execute("UPDATE users SET name = %s WHERE id = %s", (new_name, user_id))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'User updated successfully', 'user': {'id': user_id, 'name': new_name}}), 200
    
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500
    
    
if __name__ == '__main__':
    app.run(debug=True)