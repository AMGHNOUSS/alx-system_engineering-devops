#!/usr/bin/python3
"""
Gather information about Employee by passing a integer.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # URL
    url = "https://jsonplaceholder.typicode.com/"

    # Get data using API
    emp_id = sys.argv[1]
    response = requests.get(url + "users/" + emp_id)
    data = response.json()
    params = {"userId": emp_id}
    response_todos = requests.get(url + "todos", params)
    data_todos = response_todos.json()

    # Dictionary
    list0 = []
    for item in data_todos:
        dict1 = {
                'task': item['title'],
                'completed': item['completed'],
                'username': data['username']
                }
        list0.append(dict1)
    # Handle with file csv.
    filename = emp_id + ".json"
    with open(filename, mode='w', newline="") as file:
        json.dump({emp_id: list0}, file, indent=4)
