import threading 
import requests 
from bs4 import BeautifulSoup

urls = [
    'https://019aa250-77cc-7a90-9dfa-363376654c44.arena.site/',
    'https://www.langchain.com/',
    'https://github.com'
]

def fetch_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f'Fetched {len(soup.text)} characters from {url}')
    except Exception as e:
        print(f"Error fetching {url}: {e}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All URLs have been fetched.')
            
