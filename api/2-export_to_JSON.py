#!/usr/bin/python3
"""Export employee TODO list to JSON."""

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()

    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()

    data = {
        employee_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"]
            }
            for task in todos
        ]
    }

    with open(f"{employee_id}.json", "w") as file:
        json.dump(data, file)