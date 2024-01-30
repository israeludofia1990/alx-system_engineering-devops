#!/usr/bin/python3
'''extend your Python script to export data in the CSV format.'''
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))
    '''convert response to python dict'''
    user = user_response.json()
    username = user.get("username")
    todos_response = requests.get(url + "todos", params={"userid": user_id})
    todos = todos_response.json()

    '''open csv file for writing'''
    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
                ])
