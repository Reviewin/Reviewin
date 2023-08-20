#import os
#os.system("uvicorn api:api --reload")
import couchdb
import requests
n = 0
for i in range(50):
    res = requests.get('http://127.0.0.1:2223/captcha')
    if res.status_code == 200:
        n = n + 1
        print(n)
    else:
        exit()

