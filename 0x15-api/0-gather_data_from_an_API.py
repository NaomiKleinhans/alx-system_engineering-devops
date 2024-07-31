#!/usr/bin/python3

import requests
import sys

# Accept Employee ID as a Command-Line Argument
if len(sys.argv) != 2:
    print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Fetch Employee Data from the API
base_url = "https://jsonplaceholder.typicode.com/"
user_url = f"{base_url}users/{employee_id}"
todos_url = f"{base_url}todos?userId={employee_id}"

user_response = requests.get(user_url)
todos_response = requests.get(todos_url)

if user_response.status_code != 200 or todos_response.status_code != 200:
    print("Error: Unable to fetch data")
    sys.exit(1)

user = user_response.json()
todos = todos_response.json()

# Process and Display the Data
employee_name = user.get("name")
total_tasks = len(todos)
completed_tasks = [task for task in todos if task.get("completed")]
num_completed_tasks = len(completed_tasks)

print(
    f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
for task in completed_tasks:
    print(f"\t {task.get('title')}")
