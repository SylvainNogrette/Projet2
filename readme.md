# Projet2 : ETL to Book To Scrape

Le script permet la  mise en place d'une pipeline ETL pour récupérer les données concernant chaque produit répertorié sur le site Book To Scrape dans le cadre d'une veille concurentielle. Ces informations seront triés et stockés au format .csv suivant leur catégorie. Les données interessantes qui seront stockées seront :

-- l'URL de la page produit
- le code UPC de chaque produit
- le titre
- le prix hors taxes
- le prix taxes incluses
- la quantité disponible
- la description
- la catégorie d'ouvrage
- le nombre de recommandations
- le nom du fichier image stocké localement
- l'URL de l'image du produit

Comme la ligne 14 le laisse supposer, les images de chaque produits seront également récupérées et stockées localement dans un dossier Books Pictures

Chaque fois qu'une veille sera entreprise, il faudra supprimer (ou archiver) les dossiers créent lors de la veille précédente avant d'exécuter le code.

## Prérequis à l'utilisation

Le script en lui même nécessite une connexion internet pour être exécuté. Toutefois le traitement à proprement parler des csv créent pourra être effectué hors-ligne.

Python3 doit être installé sur votre ordinateur (v3.12.3). Vous pouvez vérifier votre version en tapant la commande python3 -v
Pour installer Python sous Windows, téléchargez l'installateur correspndant à votre systeme via le lien suivant :
https://www.python.org/downloads/windows/
Sous linux, exécutez la fonction apt install python3

Pour l'installation des dépendances vous devez disposer de l'installateur pip ou utilisez la commande apt install python3-xyz en remplaçant xyz par le nom de la dépendance souhaitée.
La liste des dépendances nécessaires est disponible dans le fichier requierements.txt

Git est également nécessaire pour cloner le projet sr votre machine. Pour installer la version de Git adaptée à votre configuration suivez le lien suivant et lancer l'installateur:
https://git-scm.com/downloads

## Installer le programme

Utilisez la commande suivante pour télécharger le programme.
''git clone https://github.com/SylvainNogrette/Projet2.git''

## Installer les dépendances 

Le programme utilise principalement les dépendances bs4 et csv mais vous pouvez retrouver la liste complète des dépendances dans le fichier requierement.text
Vous pouvez installer ces dépendances manuellement ou utiliser la commande depuis le dossier de travail
pip install -r requierements.txt

## Utiliser le programme 

Dans le dossier de travail, taper la commande :
 " python3 scrap.py "
 les images ainsi que les données extraites et stockées sous forme de .csv sont stockés dans les dossiers des différentes catégories
 Attention : Le script peut prendre plusieurs minutes à s'exécuter et son exécution répétée rapidement peut provoquer le bloquage temporaire de votre addresse IP et donc rendre temporairement inopérant le programme. 