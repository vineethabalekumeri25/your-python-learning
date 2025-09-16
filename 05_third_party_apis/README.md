# Simple Project: APIs

This folder contains small projects using third-party APIs with Python's `requests` library.

## Files
- **weather_app.py** → Fetches and displays live weather for a given city using OpenWeatherMap API.
- **news_fetcher.py** → Retrieves the latest news headlines using the NewsAPI.
- **README.md** → Explains how to use the scripts.

## Setup
1. Install dependencies:
   ```bash
   pip install requests


---

## 📁 `05_third_party_apis/simple_project_api/README.md`

```markdown
# Weather & News Fetcher (API Project)

## 📌 Objective
Learn how to make HTTP requests and handle JSON data by consuming public APIs from :contentReference[oaicite:0]{index=0} and :contentReference[oaicite:1]{index=1}.

---

## ⚙️ Setup Instructions
1. Get API Keys  
   - Sign up at [https://openweathermap.org/api](https://openweathermap.org/api) for a free API key.
   - Sign up at [https://newsapi.org/](https://newsapi.org/) for a free API key.
2. Add keys to a `.env` file in this folder:
OPENWEATHER_KEY=your_api_key_here
NEWSAPI_KEY=your_api_key_here
3. Run the scripts  
```bash
git clone https://github.com/<your-username>/your-python-learning.git
cd your-python-learning/05_third_party_apis/simple_project_api
python weather_app.py
# or
python news_fetcher.py

Key Features & Flow
Makes GET requests with the Requests library
Parses JSON responses
Handles API errors gracefully
Prints clean weather/news summaries

Weather in London: 23°C, Clear sky
Top News: "Python becomes #1 programming language"

simple_project_api/
│── weather_app.py
│── news_fetcher.py
└── README.md
