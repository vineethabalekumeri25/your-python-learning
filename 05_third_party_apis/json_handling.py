"""
Working with JSON data from APIs.
"""

import requests
import json

# Fetch data from a sample API
def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.ok:
        data = response.json()
        print("Raw Data:", data)

        # Convert Python dict -> JSON string
        json_string = json.dumps(data, indent=4)
        print("As JSON String:\n", json_string)

        # Convert JSON string -> Python dict
        python_dict = json.loads(json_string)
        print("Back to Python dict:", python_dict)


if __name__ == "__main__":
    fetch_data()
