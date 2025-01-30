import requests
import csv
import os
from bs4 import BeautifulSoup
import urllib.request
import re
import unicodedata

#Global variables :
urlAccueil = "http://books.toscrape.com/"

def DefineFolderName(cat,FolderNumber):
    FolderName = str(FolderNumber) + " - " + cat
    return FolderName

def BuiltDirectoryCategory(DirectoryName):

    try :
        os.mkdir(DirectoryName)
    except :
         pass
    os.chdir(DirectoryName)
    try :
        os.mkdir("Books Pictures")  
    except :
        pass        
    os.chdir('..')
    return

def DisplayCorrectString(textToDisplay):
    normalizedText = unicodedata.normalize('NFC',textToDisplay).encode('ascii','ignore').decode('utf8')
    return normalizedText

def GetBooksFromCategory(url):
    listbook = []
    for urlpage in GetAllUrlPagesFromCategories(url) :
        soup = GetSoup(urlpage)
        soupbook = soup.findAll("h3")
        try : 
            for article in soupbook:
                listbook.append(
                      urlAccueil 
                    + "catalogue/"+article.find("a").get("href").lstrip("./")
                    )
        except Exception as e :
            print(e)    
    return listbook


def GetAllUrlPagesFromCategories(firsturl):
    soup = GetSoup(firsturl)
    urlPagesFromCategories = [firsturl]
    i=1
    try :
        while soup.find("li",{"class" : "next"}) != None:
            urlPagesFromCategories.append(
                firsturl.rstrip("index.html") 
                + soup.find("li",{"class" : "next"}).find("a").get("href"))
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
        
        # Contenu de bookInfos correspondant au en-tête du fichier csv :
        # product_page_url
        # universal_product_code
        # title
        # price_including_tax
        # price_excluding_tax
        # number_available
        # product_description
        # category
        # review_rating
        # image_url
        try : 
            os.chdir("Books Pictures")
            image_file = re.sub(r'[\\/*?:"<>|]',"",str(soup.find("h1").text)) + ".jpg"
            urllib.request.urlretrieve(
                urlAccueil + soup.find("img").get("src").lstrip('./') , image_file)
            
            os.chdir('..')
        except :
            pass     
        bookInfos = []
        bookInfos.extend([
            # product_page_url
            urlbook,                                                                              
            # universal_product_code
            soup.findAll("tr")[0].find("td").text,                                                
            # title
            soup.find("h1").text,                                                                 
            # price_including_tax
            soup.findAll("tr")[3].find("td").text.strip("Â"),                                     
            # price_excluding_tax
            soup.findAll("tr")[2].find("td").text.strip("Â"),                                     
            # number_available
            soup.findAll("tr")[5].find("td").text,                                                
            # product_description
            DisplayCorrectString(soup.find("meta",{"name":"description"}).get("content").strip()),                      
            # category
            cat,                                                                                  
            # review_rating
            soup.find("div",{"class":"col-sm-6 product_main"})
                .findAll("p")[2].attrs['class'][1], 
            # image_file
            image_file,
            # image_url
            urlAccueil + soup.find("img").get("src").lstrip('./')])                               

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
        
        headers = [
            "product_page_url","universal_product_code","title",
            "price_including_tax","price_excluding_tax",
            "number_available","product_description","category",
            "review_rating","image_file","image_url"]
        j = 1
        for category , url in categoriesList :
            
            BuiltDirectoryCategory(DefineFolderName(category,j))
            os.chdir(DefineFolderName(category,j))
            j+=1
            with open(str(category)+"_books.csv","w",newline="", encoding ="utf-8") as fichier_csv :

                writer = csv.DictWriter(fichier_csv, fieldnames=headers)
                writer.writeheader()
                writer = csv.writer(fichier_csv,delimiter=",", quoting=csv.QUOTE_ALL)
                
                for bookUrl in GetBooksFromCategory(url):  
                    BuiltBookInfo = BuiltBook(category,bookUrl)          
                    writer.writerow(BuiltBookInfo)

            os.chdir('..')
        

    
    except Exception as e: 
         print(e)

else :
        print("Echec : la page n'a pas était retrouvée")

