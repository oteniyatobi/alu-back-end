#!/usr/bin/python3
"""Export employee TODO list to CSV."""
import csv
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

    with open(f"{employee_id}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
