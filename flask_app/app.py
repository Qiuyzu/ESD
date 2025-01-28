from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database / MongoDB connection configuration
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': '',  # Replace with your MySQL username
    'password': '',  # Replace with your MySQL password
    'database': 'example_db'  # Replace with your database name
}

# In-memory database for demonstration purposes
users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
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

if __name__ == '__main__':
    app.run(debug=True)