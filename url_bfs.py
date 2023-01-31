from collections import deque
import requests
from bs4 import BeautifulSoup

queue = deque()
visited = {}
token = 0

url = input("Enter the starting URL: ")
queue.append(url)

while queue:
    current_url = queue.popleft()
    print(token, current_url)
    visited[current_url] = token
    token += 1

    try:
        res = requests.get(current_url, headers={'User-Agent': 'Mozilla/5.0'})
        if res.status_code == 200 and res.headers['content-type'].startswith('text/html'):
            soup = BeautifulSoup(res.text, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                if 'href' in link.attrs:
                    new_url = link['href']
                    if new_url not in visited:
                        queue.append(new_url)
    except:
        pass
