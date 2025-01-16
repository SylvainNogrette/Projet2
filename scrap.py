import requests
import csv
import os
from bs4 import BeautifulSoup
import urllib.request
import re

urlAccueil = "http://books.toscrape.com/"
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
                listbook.append(urlAccueil + "catalogue/"+article.find("a").get("href").lstrip("./"))
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


def BuiltBook(cat,urlbook):
    soup = GetSoup(urlbook)
    try :


        bookInfos = []
        bookInfos.append(urlbook)   # product_page_url
        bookInfos.append(soup.findAll("tr")[0].find("td").text) # universal_product_code
        bookInfos.append(soup.find("h1").text)  # title
        bookInfos.append(soup.findAll("tr")[3].find("td").text.strip("Â")) # price_including_tax
        bookInfos.append(soup.findAll("tr")[2].find("td").text.strip("Â")) # price_excluding_tax
        bookInfos.append(soup.findAll("tr")[5].find("td").text) # number_available
        bookInfos.append(soup.find("meta",{"name":"description"}).get("content").strip())   # product_description
        bookInfos.append(cat)   # category
        bookInfos.append(soup.find("div",{"class":"col-sm-6 product_main"}).findAll("p")[2].attrs['class'][1])  # review_rating
        bookInfos.append(urlAccueil + soup.find("img").get("src").lstrip('./')) # image_url
    
    except Exception as e :
        print(e)
    return bookInfos

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
        headers = ["product_page_url","universal_product_code","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url"]
        for category , url in categoriesList :
            BuiltDirectoryCategory(category)
            os.chdir(category)
            with open(str(category)+"_books.csv","w") as fichier_csv :
                writer = csv.writer(fichier_csv,delimiter=',')
                writer.writerow(headers)
                for bookUrl in GetBooksFromCategory(url):
                    BuiltBookInfo = BuiltBook(category,bookUrl)
                    writer.writerow(BuiltBookInfo)
                    urllib.request.urlretrieve(BuiltBookInfo[-1], re.sub(r'[\\/*?:"<>|]',"",str(BuiltBookInfo[2]))+".jpg")
            os.chdir('..')
        

    
    except Exception as e: 
         print(e)

else :
        print("Echec : la page n'a pas était retrouvée")

# for cat, url in ca
# créer csv 
# récup info livre de la cat
#  ecrire dans le csv les infos de chaque livre
# revenir dans le directory parent
# passer à la catégorie suivante

