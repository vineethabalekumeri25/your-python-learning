"""
Examples of using the 'requests' library to work with third-party APIs.
"""

import requests

# Example 1: Simple GET request
def fetch_example():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("GitHub API Root:", response.json())
    else:
        print("Error:", response.status_code)


# Example 2: GET with query parameters
def search_repositories(query="python"):
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": "stars"}
    response = requests.get(url, params=params)
    if response.ok:
        data = response.json()
        print(response.json())
        print(f"Top repository for '{query}':", data['items'][0]['full_name'])
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    fetch_example()
    search_repositories("machine learning")
