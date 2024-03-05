import requests


def employee_data():
    url = 'http://127.0.0.1:8000/employee-list'

    response = requests.get(url)
    employees = response.json()

    return employees

