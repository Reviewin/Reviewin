import requests
import couchdb


import importlib.util
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
database = couchdb.Database('http://{module.username}:{module.password}@127.0.0.1:5984/captcha_test')
response = requests.get(f'http://admin:kolea21342@127.0.0.1:5984/captcha_test/_design/Captchadoc/_view/all_captcha')
n = 0
print(response.status_code)
print(response.json())
print(len(response.json()['rows']))
for i in range(len(response.json()['rows'])):
    print(response.json()['rows'][i]["id"])
    n = n + 1
    database.delete(database[response.json()['rows'][i]["id"]])
    print(f"Document numéro {n} supprimé")