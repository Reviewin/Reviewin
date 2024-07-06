import requests
import string
import time
import couchdb
import datetime
all_letters = list(string.ascii_lowercase)
url_possibles = []
n = 0
liste_academies = ["aix-marseille", 'besancon', "clermont-ferrand", "bordeaux", "amiens", "corse", "creteil", "dijon", "grenoble", "guadeloupe", "guyane", "la-reunion","lille", "limoges", "lyon", "martinique", "mayotte", "montpellier", "nancy-metz", "nantes", "nice", "normandie", "nouvelle-caledonie", "orleans-tours", "paris", "poitiers", "polynesie-francaise", "reims", "rennes", "saint-pierre-et-miquelon", "strasbourg", "toulouse", "versailles", "wallis-et-futuna"]
for i in range(len(liste_academies)):
    n = n + 1
    print(f"test numéro {n} commencé pour l'académie {liste_academies[i]}")
    for j in range(len(all_letters)):
        for k in range(100):
            url =  f"https://resultat-bac.linternaute.com/academie-{liste_academies[i]}/{all_letters[j]}?page={k}"
            response = requests.get(url)
            if "Selsebil" in response.text:
                print(response.text)
                print(f"{True} lettre {all_letters[j]} page numéro {k} académie {liste_academies[i]}")
                url_possibles.append(url)
            else:
                print(f"{False} lettre {all_letters[j]} page numéro {k} académie {liste_academies[i]}")
print(url_possibles)
document = {"url": url_possibles}
couchdb.Database(f"http://admin:kolea21342@127.0.0.1:5984/scrapper-bac").save(document)