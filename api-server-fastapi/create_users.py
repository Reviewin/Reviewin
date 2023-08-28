import random
import couchdb
import requests
import services
from services import generate_password, generate_random_ip, list_country
import pycountry
from pycountry import countries
import string
import importlib
import importlib.util
import passlib
from passlib.hash import pbkdf2_sha256 as sh
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
database = couchdb.Database(f"http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users")
import datetime
_domains_ = ["gmail.com", "yahoo.com", "outlook.com"]
clients = ["Windows", "Android", "Iphone","Linux"]
liste_gender  = ["M","F"]
def generate_10_countries(liste: list)->list:
    final_list = []
    for i in range(10):
        final_list.append(liste[random.randint(0, len(liste) - 1)])
    return final_list

def generate_email()->str:
    debut = []
    domain = []
    endings = []
    characters = string.digits + string.ascii_lowercase + string.ascii_lowercase.upper() 
    for i in range(random.randint(4, 15)):
        debut.append(characters[random.randint(0, len(characters) - 1)])
    username_email = "".join(debut)
    for i in range(random.randint(5, 10)):
            domain.append(characters[random.randint(0, len(characters) - 1)])
    domain_email = "".join(domain)
    for i in range(len(string.ascii_lowercase)):
        for j in range(26):
            if j <= 26:
                endings.append(string.ascii_lowercase[i] + string.ascii_lowercase[j])
    final_email = f"{username_email}@{domain_email}.{endings[random.randint(0, len(endings) - 1)]}"
    return final_email
for i in range(300):
    payload = {
        "role":"consumer",
        "age":random.randint(17,100),
        "country":generate_10_countries(list_country())[random.randint(0,9)],
        "email":f"{generate_email()}",
        "gender":liste_gender[random.randint(0,len(liste_gender)-1)],
        "password":sh.hash(generate_password()), #on hashe le mot de passe 
        "client": clients[random.randint(0, len(clients)-1)],
        "ip": sh.hash(str(generate_random_ip())),#on hashe l'ip
        "points":0,
        "language":"fr",
        "year":datetime.datetime.now().year,
        "day":datetime.datetime.now().day,
        "hour":datetime.datetime.now().hour,
        "minute":datetime.datetime.now().minute
    }
    database.save(payload)
import json
response = requests.get(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users/_all_docs?include_docs=True')
with open("C:/Users/33769/Documents/Github/Reviewin/data-science/mission.json", "w") as document:
    json.dump(response.json(), document, indent=4)




