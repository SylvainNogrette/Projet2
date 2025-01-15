import requests
import csv
from bs4 import BeautifulSoup
def prodParCategory(url) :
    response = requests.get(url)
    if response.status_code == 200:
        htmlcategory = response.text
        soup = BeautifulSoup(htmlcategory,'html.parser')
        livre = soup.find_all("h3").text
        print (livre)