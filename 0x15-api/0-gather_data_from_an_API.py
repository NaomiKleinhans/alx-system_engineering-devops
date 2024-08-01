#!/usr/bin/python3
"""
For a given employee ID, returns to-do list info
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Fetch user's to-do list
    todos_response = requests.get(
        url + "todos", params={"userId": employee_id})
    todos = todos_response.json()

    # Completed tasks
    completed_tasks = [task for task in todos if task.get("completed") is True]
    completed_tasks_titles = [task.get("title") for task in completed_tasks]

    # Output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)
    ))

    # Print titles of completed tasks with proper formatting
    for title in completed_tasks_titles:
        print("\t {}".format(title))
