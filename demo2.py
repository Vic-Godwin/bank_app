import os
import json


def save_user_data():
    user_list = []

    while True:
        name = input("Enter name (or 'quit' to exit): ")
        if name == 'quit':
            break
        email = input("Enter email: ")
        contact = input("Enter contact: ")

        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
        user_list.append(user_data)

    if os.path.exists("user_data.json"):

        with open("user_data.json", "r") as file:
            existing_data = json.load(file)
        user_list.extend(existing_data)

    with open("user_data.json", "w") as file:
        json.dump(user_list, file, indent=4)

    print("user data saved successfully")


def read_user_data():
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return

    with open("user_data.json","r") as file:
        user_list = json.load(file)
        for number,user_data in enumerate(user_list):
            print(f"NAME:Data ID: {number}\n{user_data['name']}\nEMAIL: {user_data['email']}\nCONTACT: {user_data['contact']}")
            print()
            

def edit_user_data(name):
    if not os.path.exists("user_data.json"):
        print("NO USER DATA IN DIRECTORY")
        return

    with open("user_data.json", "r") as file:
        user_list = json.load(file)

    user_found = False
    for user_data in user_list:
        if user_data['name'].lower() == name.lower():
            email = input("Enter Updated email: ")
            contact = input("Enter Updated contact: ")

            user_data['email'] = email
            user_data['contact'] = contact
            user_found = True
            break
    if not user_found:
        print("User not found")

    with open("user_data.json", "w") as file:
        json.dump(user_list, file)

    print("user data updated successfully")

found  = False
def delete_user_data(name):

    if not os.path.exists("user_data.json"):
        print("User Name Not Found")
        return

    with open("user_data.json","r") as file:
        user_list = json.load(file)

    for user_data in user_list:
        if user_data['name'].lower() == name.lower():
            user_list.remove(user_data)
            break

        else:
            print("user not found")

    with open("user_data.json","w") as file:
        json.dump(user_list, file)

    print("user successfullly deleted"
          "")







#edit_name = input("Enter username to delete: ")
#delete_user_data(edit_name)
save_user_data()
#edit_user_data(edit_name)