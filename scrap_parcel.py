import requests
import csv
from parsel import Selector

urlAccueil = "http://books.toscrape.com/"
response = requests.get(urlAccueil)
if response.status_code == 200:
    selector = Selector(text=response.text)
    print(selector)
    #crée le dictionnaire categories regroupant l'url des pages de catégories
    # categories = selector.xpath('//div[@class="side_categories"]').getall
    # print(categories)
    
    


else :
        print("Echec : la page n'a pas était retrouvée")