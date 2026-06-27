#!/usr/bin/python3
"""Export employee TODO list to JSON."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
            f"{base_url}/users/{employee_id}") as r:
        user = json.loads(r.read().decode())

    with urllib.request.urlopen(
            f"{base_url}/todos?userId={employee_id}") as r:
        todos = json.loads(r.read().decode())

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
        