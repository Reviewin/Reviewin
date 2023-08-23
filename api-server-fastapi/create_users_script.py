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
    import random 
    import pycountry
    from pycountry import countries
    final_list_of_countries_imported_uwu = []
    for loop in range(len(pycountry.countries)):
        final_list_of_countries_imported_uwu.append(list(pycountry.countries)[loop].name.upper())
    country = final_list_of_countries_imported_uwu[random.randint(0, len(final_list_of_countries_imported_uwu))]
    import random
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(random.randint(0,8)))
    payload = {
        "role":"consumer",
        "age":random.randint(17,100),
        "country":country,
        "email":f"{liste_email[i]}@",
        "gender":liste_gender[random.randint(0,len(liste_gender)-1)],
        "password":sh.hash(password), #on hashe le mot de passe 
        "client": clients[random.randint(0, len(clients)-1)],
        "ip": sh.hash(str(ip)),#on hashe l'ip
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
