import os
import json

def save_user_data(filename, user_data):

    # check if file exist and is not empty
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        existing_data = [] # store an empty list instead

    else:
        with open(filename, "r", encoding="utf_8") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = [] # if error in open file then store an empty list instead

    with open(filename, "w", encoding="utf_8") as file:
        existing_data.extend(user_data)
        json.dump(existing_data, file, indent=4)




def load_user_data(filename)
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        existing_data = []
        return existing_data

    else:
        with open(filename, "r", encoding="utf_8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                existing_data = []
                return existing_data



#dump this file when the load function is called separately
def dump_user_data(filename, data):

    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        existing_list = []
        return existing_list

    try:

        with open(filename, "w", encoding="utf_8") as file:
            json.dump(data, file, indent=4)

    except json.JSONDecodeError:
        existing_list = []
        return existing_list