#!/usr/bin/python3
# Gather information about Employee by passing a integer.

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    response = requests.get(url + "users/" + emp_id)
    data = response.json()
    params = {"userId": emp_id}
    response_todos = requests.get(url + "todos", params)
    data_todos = response_todos.json()
    a = 0
    for item in data_todos:
        if item['completed'] is True:
            a = a + 1
    print("Employee {} is done with tasks({}/{}):"
          .format(data['name'], a, len(data_todos)))
    for item in data_todos:
        if item['completed'] is True:
            print("\t {}".format(item['title']))
