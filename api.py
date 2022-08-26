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
import recaptcha_2 as _recaptcha_2
import fastapi.responses as _responses 
import random as _random
import captcha 
from captcha.image import ImageCaptcha

api = FastAPI() #on instancie 

class UserLogin(BaseModel):
    full_name: str
    e_mail: str
    password: str


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

templates = Jinja2Templates(directory="static")
api.mount("/static", StaticFiles(directory="static"), name="static")

@api.get('/signup', response_class= HTMLResponse)
async def return_html(request: Request):
    context = {'request':request}
    return templates.TemplateResponse('index_.html', context)

@api.post('/test')
async def test():
    return {"Test":"not done"}

@api.get("/recaptcha")
def get_image():
    image_path = _recaptcha_2.select_random("web")
    return _responses.FileResponse(image_path)

@api.get('/captcha')
def return_image():
    ac  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','10','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a = _random.choice(ac)
    b = _random.choice(ac)
    c = _random.choice(ac)
    d = _random.choice(ac)
    f = _random.choice(ac)
    g = _random.choice(ac)
    h = _random.choice(ac)
    random_string = a + b + c + d + f + g + h 
    random_source = random_string + '.png'
    image = ImageCaptcha(width=100, height=90)
    gen = image.generate_image(random_string)
    gen_1 = gen.save(random_source)
    return _responses.FileResponse(random_source)
    
if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 8080)
