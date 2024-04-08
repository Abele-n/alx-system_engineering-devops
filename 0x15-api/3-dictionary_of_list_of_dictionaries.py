#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({u.get("id"): [{
            "task": m.get("title"),
            "completed": m.get("completed"),
            "username": u.get("username")
        } for m in requests.get(url + "todos", params={"userId": u.get(
            "id")}).json()] for u in users}, jsonfile)
