#!/usr/bin/python3
"""Write a Python script that, using given fake REST API,
    for a given employee ID, returns information about
    his/her TODO list progress."""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    tasks_done, total_tasks = 0, 0

    # creating response objects for employee
    employee_response = \
        requests.get(f"https://jsonplaceholder.typicode.com/\
            users/{employee_id}")
    # creating dictionary objects for response objects
    employee_info = employee_response.json()

    # does name exist?
    if 'name' not in employee_info:
        print("Invalid employee ID")
        return

    # creating response objects for employee & their todo list
    todo_response = \
        requests.get(f"https://jsonplaceholder.typicode.com/\
            users/{employee_id}/todos")
    # creating dictionary objects for response objects
    todo_list = todo_response.json()


    # name variable placeholder
    employee_name = employee_info['name']

    # task incrementation
    for task in todo_list:
        total_tasks += 1
        if task['completed']:
            tasks_done += 1

    print(f"Employee {employee_name} \
        is done with tasks({tasks_done}/{total_tasks}):")

    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
