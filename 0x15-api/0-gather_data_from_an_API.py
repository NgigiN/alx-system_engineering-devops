#!/usr/bin/python3
"""
Request from API; Return TODO for an emplyee
"""
import requests
from sys import argv


def display():
    """return API data """
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (user.get('name'))
            break

    task_number = 0
    done_tasks = 0
    task_name = []
    to_dos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for to_do in to_dos.json():
        if to_do.get('userId') == int(argv[1]):
            task_number += 1
            if to_do.get('completed') is True:
                done_tasks += 1
                task_name.append(to_do.get('title'))

        print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
              done_tasks, task_number))
        for task in task_name:
            print("\t {}".format(task))


if __name__ == "__main__":
    display()
