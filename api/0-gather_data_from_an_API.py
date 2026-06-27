#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    ).json()

    done = [t for t in todos if t.get("completed")]
    print(
        f"Employee {user.get('name')} is done with tasks"
        f"({len(done)}/{len(todos)}):"
    )
    for task in done:
        print(f"\t {task.get('title')}")
        