import requests
from bs4 import BeautifulSoup

def get_page(url):
   response = requests.get(url)
   soup =BeautifulSoup(response.content,'html.parser')

   tag = soup.find_all('h4')
   for t in tag:

      print(t)
  

get_page(input("what url you want to scrape? "))