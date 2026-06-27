import json
import requests

users = requests.get(
    "https://jsonplaceholder.typicode.com/users"
).json()

todos = requests.get(
    "https://jsonplaceholder.typicode.com/todos"
).json()

data = {}

for user in users:
    data[str(user["id"])] = [
        {
            "username": user["username"],
            "task": task["title"],
            "completed": task["completed"]
        }
        for task in todos
        if task["userId"] == user["id"]
    ]

with open("todo_all_employees.json", "w") as file:
    json.dump(data, file)