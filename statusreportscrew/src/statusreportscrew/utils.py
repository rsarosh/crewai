import os
import requests

API_KEY = os.getenv("NEWSAPI_KEY")

def get_latest_stock_news_via_api(symbol, max_headlines=5):
    """
    Use NewsAPI to fetch the latest news headlines about a stock symbol.
    """
    base_url = "https://newsapi.org/v2/everything"
    query = f"{symbol} stock"
    
    params = {
        "q": query,
        "apiKey": API_KEY,
        "pageSize": max_headlines,
        "sortBy": "publishedAt",
        "language": "en",
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    news_headlines = []
    if data.get("status") == "ok":
        for article in data["articles"]:
            news_headlines.append({
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "publishedAt": article["publishedAt"]
            })
    
    return news_headlines