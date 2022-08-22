from fastapi import FastAPI 
import uvicorn
from typing import Union
from pydantic import BaseModel
from typing import Optional
import couchdb
import requests
import json
from fastapi import Request 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

api = FastAPI() #on instancie 

api.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class User_register(BaseModel):
    full_name: str
    gender: str
    age: str
    country: str
    e_mail: str
    password: str



@api.post('/test')
async def sign_up(info_user: User_register):
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/my_database_2')
    db.save(info_user.dict())
    return {"Status":"Done"}


@api.post('/users')
async def test_verification(info_user: User_register):
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/my_database_2/3b487347101b23f823ef3ca321005958')
    info_user = info_user.dict()
    res = requests.get('http://admin:kolea21342@localhost:5984/my_database_2/3b487347101b23f823ef3ca321005958')
    print(res.text)
    if len(info_user["password"]) < 8 and info_user['e_mail'] in res.text:
        return {"bad":"password","e_mail_user":"in db"}
    else:
        db.save(info_user)
        return {"Status":"Done", "e_mail_user":"not in db"}


@api.get('/login')
async def login_user():
    res = requests.get('http://admin:kolea21342@localhost:5984/db_reviewin_2/9f86611934b286b7ae19c35c6c000409')
    print(res.text)
    if "John Doe" in res.text:
        print("It's on db")
    else:
        return {"Status":"Not Done"}

#retourne la page sign up. Le sign up est géré par le serveur de l'API.
@api.get('/signup', response_class= HTMLResponse)
async def return_html():
    return templates.TemplateResponse('index_.html')
    
if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 2222)
