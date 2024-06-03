#!/usr/bin/python3
# Gather information about Employee by passing a integer.

import csv
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
    filename = emp_id + ".csv"
    with open(filename, mode='w', newline="") as file:
        for item in data_todos:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow([emp_id, data['name'], item['completed'],
                             item['title']])
