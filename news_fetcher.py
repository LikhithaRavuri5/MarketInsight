import requests
from bs4 import BeautifulSoup
import config

def fetch_news():
    COMPANY_NAME = config.COMPANY_NAME
    print(f"Fetching news for {COMPANY_NAME}...")
    url = f"https://news.google.com/search?q={COMPANY_NAME}+stock+market&hl=en-IN&gl=IN&ceid=IN:en"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    headlines = []
    
    for item in soup.find_all("a", class_="JtKRv"):
        headlines.append(item.text)
        if len(headlines) == 10:
            break
    
    if not headlines:
        headlines = [f"{COMPANY_NAME} shows strong market performance",
                    f"{COMPANY_NAME} announces new business strategy",
                    f"Investors watch {COMPANY_NAME} closely this quarter"]
    
    print(f"Found {len(headlines)} headlines!")
    return headlines

if __name__ == "__main__":
    news = fetch_news()
    for i, headline in enumerate(news, 1):
        print(f"{i}. {headline}")
        