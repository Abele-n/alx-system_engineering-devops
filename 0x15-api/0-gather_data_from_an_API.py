#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import sys
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url="users/{}".format(sys.argv[1])).json()
    todos = requests.get(url="todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for m in todos if m.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(todos)))
    [print("\t {}".format(h)) for h in completed]
