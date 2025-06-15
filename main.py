import requests
from bs4 import BeautifulSoup
import os

WEBHOOK_URL = os.getenv(https://discord.com/api/webhooks/1383423287597600899/btcn7qi2xqY7p8TeQQ-t6xKICo1464Jksym8JtYEpknToHeEwjyB2p-KIudZ7X-yxWnA)

def fetch_news():
    url = 'https://www.investing.com/commodities/gold-news'
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    news_items = soup.select('.textDiv')

    result = []
    for item in news_items[:3]:
        title = item.find('a').get_text(strip=True)
        link = 'https://www.investing.com' + item.find('a')['href']
        summary = item.find('p').get_text(strip=True) if item.find('p') else ''
        result.append((title, link, summary))
    return result

def send_to_discord(news):
    for title, link, summary in news:
        data = {
            "username": "Gold Bot",
            "embeds": [{
                "title": title,
                "url": link,
                "description": summary,
                "color": 15844367
            }]
        }
        requests.post(WEBHOOK_URL, json=data)

if __name__ == "__main__":
    send_to_discord(fetch_news())
