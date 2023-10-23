#!/usr/bin/python3
"""
This will be using a REST API, for a given employee ID and
returns information about his/her TODO list progress
"""

import json
import requests

if __name__ == '__main__':
    users = requests.get("http://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    userdict = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    todo = requests.get("http://jsonplaceholder.typicode.com/todos",
                        verify=False).json()

    for task in todo:
        taskdict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": usernamedict.get(uid)
        }
        uid = task.get("userId")

        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)
