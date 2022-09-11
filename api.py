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

class recaptcha(BaseModel):
    captcha_value:  str



class Recaptcha_2(BaseModel):
    recaptcha_2: str


@api.post('/test')
async def sign_up(info_user: User_register):
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/my_database_2')
    db.save(info_user.dict())
    return {"Status":"Done"}


@api.post('/abc')
async def captcha(info_captcha: Recaptcha_2):
    info_captcha = info_captcha.dict()
    url = 'http://admin:kolea21342@localhost:5984/captcha_test/_all_docs?include_docs=true'
    res = requests.get(url)
    if info_captcha['recaptcha_2'] in res.text:
        return {"Status":"Checked"}
    else:
        return {"Status":"Captcha invalid"}

@api.post('/check')
async def something():
    res = requests.get('http://admin:kolea21342@localhost:5984/captcha_test/_all_docs?include_docs=true')
    if {"ca"} in res.text:
        return {"Status":"Done"}
    else:
        return {"Status":"Not Done"}

@api.post('/users')
async def test_verification(info_user: User_register):
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/reviewin_users/')
    info_user = info_user.dict()
    res = requests.get('http://admin:kolea21342@localhost:5984/reviewin_users/_all_docs?include_docs=true')
    print(res.text)
    if info_user["password"] > 8 and info_user["e_mail"] not in res.text:
        db.save(info_user)
        return {"Status":"Done"}
    elif info_user["password"] > 8 and info_user["e_mail"] in res.text:
        return {"e_mail":"already used"}
    elif info_user["password"] < 8 and info_user["e_mail"] in res.text:
        return {"password":"invalid", "e_mail":"already exists"}
    elif info_user["password"] < 8 and info_user["e_mail"] not in res.text:
        return {"Status":"Password invalid"}
    else:
        return False



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
async def return_image():
    ac  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','10','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a = _random.choice(ac)
    b = _random.choice(ac)
    c = _random.choice(ac)
    d = _random.choice(ac)
    f = _random.choice(ac)
    g = _random.choice(ac)
    h = _random.choice(ac)
    random_string = a + b + c + d + f + g + h
    captcha_value = json.dumps(random_string)
    print(captcha_value)
    json_object = {"captcha_value":captcha_value}
    res = requests.post('http://admin:kolea21342@localhost:5984/captcha_test', json=json_object)
    random_source = random_string + '.png'
    image = ImageCaptcha(width=100, height=90)
    gen = image.generate_image(random_string)
    gen_1 = gen.save(random_source)
    return _responses.FileResponse(random_source)

@api.post('/check_captcha')
async def check_captcha(captcha: recaptcha):
    captcha = captcha.dict()
    url = 'http://admin:kolea21342@localhost:5984/captcha_test/_all_docs?include_docs=true'
    res = requests.get(url)
    print(res.text)
    if captcha['input_'] in res.text:
        return {"Status":"Captcha passed"}
    else:
        return {"Status":"Not Done"}



@api.get("/ver")
def s():
    return {"s":"s"}


@api.get('/captchaa')
async def return_image():
    ac  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','10','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a = _random.choice(ac)
    b = _random.choice(ac)
    c = _random.choice(ac)
    d = _random.choice(ac)
    f = _random.choice(ac)
    g = _random.choice(ac)
    h = _random.choice(ac)
    random_string = a + b + c + d + f + g + h 
    serialize = json.dumps(random_string)
    random_source = random_string + '.png'
    image = ImageCaptcha(width=100, height=90)
    image_1 = image.generate_image(random_string).save(random_source)
    database = captcha_database = couchdb.Database('http://admin:kolea21342@localhost:5984/captcha_test')
    print(serialize)
    return _responses.FileResponse(json.dumps(random_source))

@api.post('/verify_captcha')
async def verify_captcha_test():
    captcha_database = couchdb.Database('http://admin:kolea21342@localhost:5984/captcha_test/_all_docs?include_docs=true')
    ma_variable = requests.get('http://admin:kolea21342@localhost:5984/captcha_test/_all_docs?include_docs=true')
    if captcha.dict() in ma_variable:
        return {"Captcha":"good"}
    else:
        return {"Not good captcha":"don't let sign up"}

@api.post('/signin')
async def sign_in(info_login: UserLogin):
    info_login = info_login.dict()
    url = 'http://admin:kolea21342@localhost:5984/verification/_design/newDesignDoc/_view/new-view?keys=\[\"Ayoub\",\"ayoub_semsar@yahoo.com\",\"kolea21342\"\]'
    res = requests.get(url)
    print(res.text)
    verification = res.text
    if info_login['full_name'] and info_login['e_mail'] and info_login['password'] in verification:
        print("it works")
        return {"Status":"Done"}
    else:
        print("it doesn't work")
        return {"Status":"Not done"}

@api.get('/test_login')
async def return_som():
    return {"Hello":"World"}

@api.post('/test_something')
async def return_something(info_login: UserLogin):
    return True



if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 2222)
