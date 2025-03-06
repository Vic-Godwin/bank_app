import os
import json

def save_user_data(filename, user_data):
    """Save user data to a JSON file, appending to existing data if present."""
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        existing_data = []
    else:
        with open(filename, "r", encoding="utf-8") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []

    existing_data.extend(user_data)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)

def load_user_data(filename):
    """Load user data from a JSON file."""
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []

    with open(filename, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def dump_user_data(filename, user_data):
    """Overwrite a JSON file with new user data."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=4)
