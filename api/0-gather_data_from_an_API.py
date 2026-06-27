#!/usr/bin/python3
"""
Gather data from an API for a given employee.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    completed = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(completed),
            len(todos)
        )
    )

    for task in completed:
        print("\t {}".format(task.get("title")))