#import os
#os.system("uvicorn api:api --reload")
import requests
import random
import couchdb
import requests
import importlib.util
import services
from services import choose_country, generate_random_ip, generate_password
import passlib
import datetime
import string
import random 
from passlib.hash import pbkdf2_sha256 as sh
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
response = requests.get(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users/_all_docs')
liste_email = ['Billel','samira', 'soundous', 'ayoub', 'soundouse', 'tarek', 'paul', 'riyad', 'robert', 'bboy']
database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users')
_list_not_deleted = []
for i in range(len(response.json()['rows'])):
    print(response.json()['rows'])
    print(response.json()['rows'][i]['key'])
    print(response.json()['rows'][i]['id'])
    database.delete(database[str(response.json()['rows'][i]["id"])])
    print(f"document number {i} deleted")
domains = ["gmail.com", "yahoo.com", "outlook.com"]
clients = ["Windows", "Android", "Iphone","Linux"]
liste_gender = ["M","F"]
for i in range(len(liste_email)):
    payload = {
        "role":"consumer",
        "age":random.randint(17,100),
        "country":str(choose_country),
        "email":f"{liste_email[i]}@",
        "gender":liste_gender[random.randint(0,len(liste_gender)-1)],
        "password":sh.hash(str(generate_password())), #on hashe le mot de passe 
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
    print(f"{payload['email']}Saved")
#création d'email full inscriptions
