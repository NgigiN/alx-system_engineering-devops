#!/usr/bin/python3
"""
Requests from API; Return TODO for an emplyee then export to CSV"""

import csv
import requests
from sys import argv


def to_csv():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    task_status = []

    to_dos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for to_do in to_dos.json():
        if to_do.get('userId') == int(argv[1]):
            task_status.append((to_do.get('completed'), to_do.get('title')))

    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in task_status:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    to_csv()
