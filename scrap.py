import requests
import csv
from bs4 import BeautifulSoup
from recup_prodParCategory import prodParCategory


urlAccueil = "http://books.toscrape.com/"
response = requests.get(urlAccueil)
if response.status_code == 200:
    htmlAccueil = response.text
    soup = BeautifulSoup(htmlAccueil,"html.parser")
    ulcategories = soup.find("ul", {"class":"nav nav-list"})
    try : 
        i=0
        dictcategory= []
        for a in ulcategories.findAll("a"):
            if i == 0 :
                 i=i+1
                 continue
            else :
                urlcategory = urlAccueil + a.get("href")
                dictcategory[a.text.strip()]= urlcategory
                i=i+1

        print (dictcategory)
    
    except Exception as e: 
         print(e)

else :
        print("Echec : la page n'a pas était retrouvée")
# for cat, url in dictcategory :
#      print(cat, url)
