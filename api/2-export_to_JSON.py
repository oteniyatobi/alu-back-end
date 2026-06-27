#!/usr/bin/python3
"""Export employee TODO list to JSON."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    ).json()

    username = user.get("username")
    data = {
        str(employee_id): [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    with open(f"{employee_id}.json", "w") as f:
        json.dump(data, f)
        