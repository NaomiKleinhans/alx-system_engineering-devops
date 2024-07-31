#!/usr/bin/python3
import requests
import sys


def fetch_employee_tasks(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_url = f"{base_url}users/{employee_id}"
    user_response = requests.get(user_url)

    # Check if the user exists
    if user_response.status_code != 200:
        print("Error: Unable to fetch data")
        sys.exit(1)

    # Fetch todo tasks for the user
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    # Check if todos were fetched successfully
    if todos_response.status_code != 200:
        print("Error: Unable to fetch data")
        sys.exit(1)

    # Parse the user and todos data
    user = user_response.json()
    todos = todos_response.json()

    # Extract necessary details
    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]
    num_completed_tasks = len(completed_tasks)

    # Print the formatted output
    print(
        f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        fetch_employee_tasks(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
