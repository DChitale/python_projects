from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

f=open("result.txt","w")
visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed for {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('a')  # Fixed typo here
        urls = []
        for tag in a_tag:
            href = tag.get('href')
            if href is not None and href != " ":
                urls.append(href)
        # print(urls)

        
        for url2 in urls:
            if url2 not in visited_urls:
                visited_urls.add(url2)
                
                url_join=urljoin(url, url2)
                if keyword in url_join:
                    print(url_join)
                    f.write(url2)
                    spider_urls(url_join, keyword)
    else:
        pass

url = input("what url you want to scrape? ")
keyword = input("what keyword you want to search? ")

spider_urls(url, keyword)