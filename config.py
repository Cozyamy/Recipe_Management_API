import os
import json

DATABASE_FILE = "database.json"

def load_database():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as file:
            json.dump({"recipes": [], "ingredients": []}, file)
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)

def save_database(database):
    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file)