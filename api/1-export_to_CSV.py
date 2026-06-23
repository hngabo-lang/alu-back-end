#!/usr/bin/python3
"""
Exports a given employee's TODO list progress to a CSV file.

Usage:
    python3 1-export_to_CSV.py EMPLOYEE_ID

Creates USER_ID.csv with the format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""
import csv
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

    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo.get("completed"),
                todo.get("title"),
            ])
