#!/usr/bin/python3
'''extend your Python script to export data in the CSV format.'''
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_id = sys.argv[1]
    url = base_url + "/" + user_id

    user_response = requests.get(url)
    '''convert response to python dict'''
    user = user_response.json()
    username = user.get("username")
    todos_url = url + "/todos"
    response = requests.get(todos_url)
    todos = response.json()

    '''open csv file for writing'''
    with open("{}.csv".format(user_id), "w") as csv_file:
        for todo in todos:
            csv_file.write('"{}","{}","{}","{}"\n'
                          .format(user_id, username, todo.get('completed'),
                               todo.get('title')))
