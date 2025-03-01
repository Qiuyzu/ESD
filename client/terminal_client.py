import requests

def create_user(user_id, name):
    response = requests.post('http://127.0.0.1:5000/users', json={'id': user_id, 'name': name})
    if response.status_code == 201:
        print(f"User {user_id} created successfully")
    else:
        print(f"Error in user creation: {response.json}")

if __name__ == "__main__":
    while True:
        print("========== User Management Portal =============")
        print("1. Create new user")
        print("2. Retrieve existing user")
        print("3. Exit")
        option = input("Please enter your option: ")
        if int(option) == 1:
            id = input ("Enter id: ")
            name = input ("Enter username: ")
            create_user(id, name)
        elif int(option) == 2:
            print("Getting user...")
        elif int(option) == 3:
            break
        else:
            print("The option you have entered is invalid.")
