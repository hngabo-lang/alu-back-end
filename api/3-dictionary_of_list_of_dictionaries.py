#!/usr/bin/python3
"""
Exports all employees' TODO list progress to a JSON file.

Fetches all users and all todos from the JSONPlaceholder API,
groups the todos by user ID, and writes them to
todo_all_employees.json in the format:

{
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    ...
}
"""
import json
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(url):
    """Fetch a URL and return the parsed JSON response."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())


if __name__ == "__main__":
    users = get_json("{}/users".format(BASE_URL))
    todos = get_json("{}/todos".format(BASE_URL))

    # Map user id -> username
    usernames = {user["id"]: user["username"] for user in users}

    # Build the dictionary of lists of dictionaries
    all_tasks = {}
    for todo in todos:
        user_id = str(todo["userId"])
        username = usernames.get(todo["userId"], "")
        task_entry = {
            "username": username,
            "task": todo["title"],
            "completed": todo["completed"],
        }
        all_tasks.setdefault(user_id, []).append(task_entry)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
