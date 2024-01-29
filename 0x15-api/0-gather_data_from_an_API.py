#!/usr/bin/python3
"""
Return information for a given employee ID.

About his/her TODO list progress from a REST API.
"""
import requests
from sys import argv


def fetch_data(employee_id):
    """
    Fetches information about a given employee's TODO list progress
    and prints the details to the console.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Construct URLs for employee and todos data
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = \
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Make a GET request to the specified URL for employee data
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    # Extract employee name
    employee_name = employee_data.get('name')

    # Make a GET request to the specified URL for todos data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Initialize counters for completed tasks and all tasks
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    all_tasks = len(todos_data)

    # Print employee progress information
    info = f"Employee {employee_name} is done with \
tasks({completed_tasks}/{all_tasks}):"
    for todo in todos_data:
        if todo["completed"]:
            info += f"\n\t{todo['title']}"

    print(info)


if __name__ == "__main__":
    # Get the employee ID from the command line argument
    employee_id = int(argv[1])

    # Call the function to fetch todo list progress for the specified employee
    fetch_data(employee_id)
