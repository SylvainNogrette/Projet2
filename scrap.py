import requests
import csv
from parsel import Selector

url = "http://books.toscrape.com/"
text = requests.get(url).text
selector = Selector(text=text)
selector.xpath('//h1/text()').re(r'\w+')