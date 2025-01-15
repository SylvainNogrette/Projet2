import requests
import csv
import os
from bs4 import BeautifulSoup
from recup_prodParCategory import prodParCategory
def BuiltDirectoryCategory(cat):
    try :
        os.mkdir(cat)
    except :
         pass
    os.chdir(cat)          
    os.chdir('..')
    return
def GetBooksFromCategory(url):
    listbook = []
    for urlpage in GetAllUrlPagesFromCategories(url) :
        soup = GetSoup(urlpage)
        soupbook = soup.findAll("h3")
        try : 
            for article in soupbook:
                listbook.append(article.find("a").get("href"))
        except Exception as e :
            print(e)    
    return listbook
def GetAllUrlPagesFromCategories(firsturl):
    soup = GetSoup(firsturl)
    urlPagesFromCategories = [firsturl]
    i=1
    try :
        while soup.find("li",{"class" : "next"}) != None:
            urlPagesFromCategories.append(firsturl.rstrip("index.html") + soup.find("li",{"class" : "next"}).find("a").get("href"))
            soup = GetSoup(urlPagesFromCategories[i])
            i+=1
        return urlPagesFromCategories
    except Exception as e :
        print (e)

def GetSoup(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        return BeautifulSoup(html,"html.parser")
    else :
        print ("Page inexistante")


def BuiltBook(urlbook):
    soup = GetSoup(urlbook)
    try :
        listinfo = {}
        listinfo["product_page_url"] = urlbook
        listinfo["universal_product_code"] = ""
        listinfo["title"] = ""
        listinfo["price_including_tax"] = ""
        listinfo["price_excluding_tax"] = ""
        listinfo["number_available"] = ""
        listinfo["product_description"] = ""
        listinfo["category"] = ""
        listinfo["review_rating"] = ""
        listinfo["image_url"] = ""
        

    
    except Exception as e :
        print(e)

urlAccueil = "http://books.toscrape.com/"
response = requests.get(urlAccueil)
if response.status_code == 200:
    htmlAccueil = response.text
    soup = BeautifulSoup(htmlAccueil,"html.parser")
    ulcategories = soup.find("ul", {"class":"nav nav-list"})
    try : 
        i=0
        categoriesList= []
        for a in ulcategories.findAll("a"):
            tempdict = []
            if i == 0 :
                 i=i+1
                 continue
            else :
                urlcategory = urlAccueil + a.get("href")               
                tempdict.append(a.text.strip())
                tempdict.append(urlcategory)
            categoriesList.append(tempdict)
        # listEverybooks =[]
        # for cat , url in categoriesList :
        #     for elt in GetBooksFromCategory(url):
        #         listEverybooks.append(elt)
        # print(len(listEverybooks))

    
    except Exception as e: 
         print(e)

else :
        print("Echec : la page n'a pas était retrouvée")

for cat, url in categoriesList :
       BuiltDirectoryCategory(cat)

# ###Créer les directories
# lister les urls des livres de la categorie
# changer le dir courant sur celui de la cat
# créer csv 
# récup info livre de la cat
#  ecrire dans le csv les infos de chaque livre
# revenir dans le directory parent
# passer à la catégorie suivante

