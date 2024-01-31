#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
'''
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/user"
    user_id = sys.argv[1]
    url = base_url + "/" + user_id
    url_response = requests.get(url)
    username = url_response.json().get('username')

    todos_url = url + "/todos"
    todos_responce = requests.get(todos_url)
    todos = todos_responce.json()
    data_to_export = {user_id: []}
    for todo in todos:
        task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
                }
        data_to_export[user_id].append(task_info)
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile)
