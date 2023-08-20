import datetime
from datetime import datetime
import couchdb
import requests
import os
from datetime import timedelta 
while True:
    database = couchdb.Database(f"http://admin:kolea21342@127.0.0.1:5984/captcha_test")
    response = requests.get(f"http://admin:kolea21342@127.0.0.1:5984/captcha_test/_design/all_captcha/_view/all_captcha")
    date_now = datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
    if response.status_code == 200:
        for i in range(len(response.json()['rows'])):
            captcha = response.json()["rows"][i]["captcha_value"]
            path = f"C:/Users/33769/Desktop/Images_Captcha/{captcha}.png"
            datetime_past = datetime(int(response.json()["rows"][i]["year"], int(response.json()["rows"][i]["month"],int(response.json()["rows"][i]["day"]), int(response.json()["rows"][i]["hour"], int(response.json()["rows"][i]["minute"], int(response.json()["rows"][i]["second"]))))))
            time_diff = date_now - datetime
            if time_diff >= timedelta(seconds=10):
                os.delete(path)
                database.delete(database[str(response.json()["rows"][i]["id"])])
                print(f"Document numéro {i} supprimé")
            else:
                pass
    else:
        continue





