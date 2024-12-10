import requests
from bs4 import BeautifulSoup

url ="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

response = requests.get(url)

if response.ok:
   # print(response.headers) #renvoie les en-têtes
    print(response.content)
