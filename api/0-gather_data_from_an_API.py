#!/usr/bin/python3
"""
Gathers data from the JSONPlaceholder API for a given employee ID
and displays their TODO list progress.

Usage:
    python3 0-gather_data_from_an_API.py EMPLOYEE_ID
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

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
