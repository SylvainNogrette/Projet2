import requests
import csv
from parsel import Selector

urlAccueil = "http://books.toscrape.com/"
response = requests.get(urlAccueil)
if response.status_code == 200:
    htmlAccueil = response.text
    selector = Selector(text=htmlAccueil)
    categorie = selector.xpath('//div[@class="nav nav-list"]/ul/li/a/href/text()').getall
    print(categorie)
    # for li in selector.css("ul class = "nav nav-list"")
    #     # stocker les href dans un dico trouver une methode type append
    


else :
        print("Echec : la page n'a pas était retrouvée")