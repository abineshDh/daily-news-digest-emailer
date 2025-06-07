# news_fetcher.py
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

def get_headlines():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    
    try:
        data = response.json()
    except Exception as e:
        print("Failed to parse JSON:", e)
        return []   

    # Retry if the initial request fails
    retries = 3
    attempt = 0
    while (response.status_code != 200 or "articles" not in data) and attempt < retries:
        print(f"Error fetching news. Status: {response.status_code}")
        print("Response JSON:", data)
        attempt += 1
        time.sleep(2)
        response = requests.get(url)
        try:
            data = response.json()
        except Exception as e:
            print("Failed to parse JSON:", e)
            return []
    if response.status_code != 200 or "articles" not in data:
        return []

    headlines = []

    for article in data["articles"][:5]:
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown Source")
        url = article.get("url", "")
        published = article.get("publishedAt", "No date")
        formatted = f"<h2>{title}</h2>\n<h4>{source}</h4>\n<h5>{published}</h5>\n<a href='{url}'>{url}</a>\n"
        headlines.append(formatted)

    return headlines

# Temporary for debug
# if __name__ == "__main__":
#     headlines = get_headlines()
#     for line in headlines:
#         print(line)
