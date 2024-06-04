#!/usr/bin/python3
"""
Gather information about Employees.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # URL
    url = "https://jsonplaceholder.typicode.com/"

    # Get data using API
    response = requests.get(url + "users")
    users = response.json()

    # Dictionary

    data_to_export = {}
    for user in users:
        user_id = user["id"]
        user_url = url + f"todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]
    # Handle with file csv.
    filename = "todo_all_employees.json"
    with open(filename, mode='w', newline="") as file:
        json.dump(data_to_export, file, indent=4)
