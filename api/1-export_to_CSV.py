#!/usr/bin/python3
"""Export employee TODO list to CSV."""
import csv
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
    filename = f"{employee_id}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
            