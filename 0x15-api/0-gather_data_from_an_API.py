#!/usr/bin/python3
'''returns information about his/her TODO list progress.'''
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    api_responce = requests.get(base_url + "users/{}".format(employee_id))

    user_json = api_responce.json()
    req_param = {"userid": employee_id}
    get_todos = requests.get(base_url + "todos", params=req_param)
    todos_json = get_todos.json()
    completed = []
    for todo in todos_json:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{})"
          .format(user_json.get("name"), len(completed), len(todos_json)))

    for complete in completed:
        print("\t {}".format(complete))
