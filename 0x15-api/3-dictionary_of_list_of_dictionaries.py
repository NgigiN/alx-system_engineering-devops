#!/usr/bin/python3
"""
Request from API; Return TODO for an employee
Export data to JSON
"""
import json
import requests


def all_to_json():
    users = []
    userss = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in userss.json():
        users.append((u.get('id'), u.get('username')))
    status = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        status.append((t.get('userId'),
                       t.get('completed'),
                       t.get('title')))

    """export to json"""
    data = dict()
    for u in users:
        t = []
        for task in status:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    all_to_json()
