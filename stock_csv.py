import csv

def stockDansCsv(dict) :
    for keys in dict :
        with open (dict.get(keys),'w') as fichier.csv :