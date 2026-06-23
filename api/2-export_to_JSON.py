#!/usr/bin/python3
"""
Exports a given employee's TODO list progress to a JSON file.

Usage:
    python3 2-export_to_JSON.py EMPLOYEE_ID

Creates USER_ID.json with the format:
    {"USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        ...
    ]}
"""
import json
import sys
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(url):
    """Fetch a URL and return the parsed JSON response."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user = get_json("{}/users/{}".format(BASE_URL, employee_id))
    todos = get_json("{}/todos?userId={}".format(BASE_URL, employee_id))

    username = user.get("username")

    tasks = [
        {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username,
        }
        for todo in todos
    ]

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)
