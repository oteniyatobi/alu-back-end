#!/usr/bin/python3

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

    completed = [task for task in todos if task["completed"]]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"], len(completed), len(todos)
        )
    )

    for task in completed:
        print("\t {}".format(task["title"]))