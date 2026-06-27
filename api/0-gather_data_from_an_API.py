#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""
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

    done = [t for t in todos if t.get("completed")]
    print(
        f"Employee {user.get('name')} is done with tasks"
        f"({len(done)}/{len(todos)}):"
    )
    for task in done:
        print(f"\t {task.get('title')}")
