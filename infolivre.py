import requests
from bs4 import BeautifulSoup

def parse_url(url) :
    response = requests.get(url)
    if response.code_status == 200 :
        soup = BeautifulSoup(url,'html.parser')
        return soup     
        
