#!/usr/bin/python3
"""Export all employees TODO lists to JSON."""
import json
import urllib.request


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(f"{base_url}/users") as r:
        users = json.loads(r.read().decode())

    with urllib.request.urlopen(f"{base_url}/todos") as r:
        todos = json.loads(r.read().decode())

    data = {}
    for user in users:
        uid = user.get("id")
        username = user.get("username")
        data[str(uid)] = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
            }
            for t in todos if t.get("userId") == uid
        ]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)