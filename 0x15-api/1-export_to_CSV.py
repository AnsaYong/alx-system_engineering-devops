#!/usr/bin/python3
"""For a given employee ID, sends a request that returns
information about his/her TODO list progress.
"""
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    """
    Describes the TODO progress of the specified
    employee. It uses data obtained from a URL
    through a REST API

    Argument:
        employee_id: the employee ID
    Returns:
        Text to stdout
    """
    # URLs for employee and todos data
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Make a GET request to the specified URL
    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    # Check if both requests were successful (status code 200)
    if (employee_response.status_code == 200 and
            todos_response.status_code == 200):
        # Parse JSON data for employee and todos
        employee_data = employee_response.json()
        todos_data = todos_response.json()

        # Extract employee name
        employee_name = employee_data.get('name')

        # Initialize counters for completed tasks and all tasks
        completed_tasks = 0
        all_tasks = 0

        # Create a list to store task data
        task_data_list = []

        # Handle the returned todo data
        for data_dict in todos_data:
            if data_dict.get('userId') == employee_id:
                all_tasks += 1
                completed_status = str(data_dict.get('completed'))
                task_title = data_dict.get('title')

                # Append task data to the list
                task_data_list.append([str(employee_id), employee_name, completed_status, task_title])

                if data_dict.get('completed'):
                    completed_tasks += 1

        # Print progress to stdout
        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, completed_tasks, all_tasks))

        for data_dict in todos_data:
            if (data_dict.get('userId') == employee_id and
                    data_dict.get('completed')):
                print("\t" + " " + data_dict.get('title'))

        # Write task data to a CSV file
        write_to_csv(employee_id, task_data_list)


def write_to_csv(employee_id, task_data_list):
    """
    Writes task data to a CSV file.

    Arguments:
        employee_id: the employee ID
        task_data_list: list containing task data
    """
    # CSV file name
    csv_filename = f"{employee_id}.csv"

    # Writing to CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(task_data_list)

    print(f"\nTask data exported to {csv_filename}")


if __name__ == "__main__":
    # Get the employee ID from the command line argument
    employee_id = int(sys.argv[1])

    # Call the function to get todo list progress for the specified employee
    get_employee_todo_progress(employee_id)
