#!/usr/bin/python3
"""Provides a function that uses a given employee ID to
extract and return their TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Extracts and returns an employees TODO list
    progress based on their employee ID

    Argument:
        employee_id: The employees ID
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data["name"]
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo["completed"])

        print(f"Employee {employee_name} is done with \
              tasks({completed_tasks}/{total_tasks}):")

        for todo in todos_data:
            if todo["completed"]:
                print(f"\t {todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
