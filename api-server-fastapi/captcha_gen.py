import requests
import couchdb
import importlib.util 
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)


database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/captcha_test')
response = requests.get(f'http://{module.username}:{module.password}@127.0.0.1:5984/captcha_test/_all_docs')

for i in range(len(response.json()['rows'])):
    if response.json()['rows'][i]['id'] == "_design/Captchadoc":
        pass
    else:
        database.delete(database[response.json()['rows'][i]['id']])
        print(f"{i} deleted")
n = 0
for i in range(5):
    n = n + 1
    print(n)
    response = requests.get("http://127.0.0.1:2223/captcha")