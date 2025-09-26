"""
News Fetcher using a free API.
Replace 'YOUR_API_KEY' with a real key from https://newsapi.org/
"""

import requests

API_KEY = "f8702c9972194811aa8b1e614f201716"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(country="us"):
    params = {"country": country, "apiKey": API_KEY}
    response = requests.get(BASE_URL, params=params)
    if response.ok:
        data = response.json()
        print("Top Headlines:")
        for article in data["articles"][:5]:
            print("-", article["title"])
    else:
        print("Error fetching news:", response.status_code)

if __name__ == "__main__":
    fetch_news()
