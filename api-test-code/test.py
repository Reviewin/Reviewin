import requests
import couchdb
database = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/captcha_test')
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