import requests

def create_user(user_id, name):
    response = requests.post('http://127.0.0.1:5000/users', json={'id': user_id, 'name': name})
    if response.status_code == 201:
        print(f"User {user_id} created successfully")
    else:
        print(f"Error in user creation: {response.json}")

if __name__ == "__main__":
    print("========== Create user =============")
    id = input ("Enter id: ")
    name = input ("Enter username: ")
    create_user(id, name)