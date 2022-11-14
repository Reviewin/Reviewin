from fastapi import FastAPI, UploadFile, File, responses
import uvicorn
from typing import Union
from pydantic import BaseModel
from typing import Optional
import shutil
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
from deta import Drive
import os
from PIL import Image
from deta import Deta 
from deta import Drive
import aiofiles
import os

api = FastAPI() #on instancie 


class logout(BaseModel):
    e_mail: str

class sessions(BaseModel):
    e_mail: str
    password: str
    token: str

class UserLogin(BaseModel):
    e_mail: str
    password: str

class logoutf(BaseModel):
    token: str

class load_(BaseModel):
    token: str

class User_register(BaseModel):
    gender: str
    age: str
    country: str
    e_mail: str
    password: str
    points: int

class recaptcha(BaseModel):
    captcha_value:  str

class verification(BaseModel):
    e_mail: str
    age: str
    gender: str
    password: str
    country: str

class user__(BaseModel):
    e_mail: str

class Recaptcha_2(BaseModel):
    captcha_value: str


@api.post("/products")
async def create_upload_file(file: UploadFile = File(...)):
    ac =  ['0','1','2','3', '4', '5', '6', '7', '8', '9']
    a = _random.choice(ac)
    b = _random.choice(ac)
    c = _random.choice(ac)
    d = _random.choice(ac)
    e = _random.choice(ac)
    f = _random.choice(ac)
    g = _random.choice(ac)
    h = _random.choice(ac)
    i = _random.choice(ac)
    j = _random.choice(ac)
    random_id = a  + b + c + d + e + f + g + h + i + j + '.png'
    file.filename = random_id
    file_location = f"C:/Users/33769/Desktop/Reviewin/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}


@api.get('/products/{id_}')
async def get_produtcts(id_: int):
    image = str(id_) + '.png'
    return _responses.FileResponse(image)

@api.get('/products')
async def list_products():
    path = "C:/Users/33769/Desktop/Reviewin"
    valid_extension = '.png'
    files = os.listdir(path)
    return files


@api.post('/reviewin_users')
async def sign_up(info__: User_register):
    info__ = info__.dict()
    user_e_mail = info__['e_mail']
    url = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_users/_design/design_users/_view/Users?key=' + '"' + user_e_mail + '"'
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/reviewin_users')
    res = requests.get(url)

    if user_e_mail not in res.json():
        if len(info__['password']) > 8 and info__['points'] == 0:
            print("User registered")
            db.save(info__)
            return {"User":"Saved"}
            if db.save(info__):
                print('user registered')
                return {"User":"registered"}
            else:
                return {"User":"not registered"}
        else:
            return {"Password":"Not valid"}
    else:
        return {"Status":"Not done"}


@api.post('/logout')
async def logout(logout_: logoutf):
    logout_ = logout_.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key=' + '"' + logout_['token'] + '"'
    response = requests.get(url)
    doc = response.json()
    print(doc)
    id_ = doc['rows'][0]['id']
    print(id_)
    couch = couchdb.Server('http://admin:kolea21342@127.0.0.1:5984/')
    db = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/sessions')
    db.delete(db[str(id_)])
    if db.delete(db[str(id_)]):
        return {"Status":"Done"}
    else:
        return {"Status":"Not done"}


@api.post('/verify_captcha')
async def verify_captcha_test(captcha: Recaptcha_2):
    captcha = captcha.dict()
    captcha_value = captcha['captcha_value']
    url = 'http://admin:kolea21342@127.0.0.1:5984/captcha_test/_design/Captchadoc/_view/captcha_test?key=' + "%22\%22" + captcha_value + "\%22%22"
    print(url)
    ma_variable = requests.get(url)
    if captcha_value in ma_variable.text:
        print("Captcha good")
        return {"Captcha":"good"}
    else:
        return {"Not good captcha":"don't let sign up"}


@api.post('/load')
async def load_(load_data: load_):
    load_data = load_data.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key=' + '"' + load_data['token'] + '"'
    res = requests.get(url)
    doc = res.json()
    print(doc)
    print(doc['rows'][0]['key'])
    return doc


@api.post('/users')
async def test_verification(info_user: User_register):
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/reviewin_users/')
    info_user = info_user.dict()
    res = requests.get('http://admin:kolea21342@localhost:5984/reviewin_users/_all_docs?include_docs=true')
    print(res.text)
    if info_user["e_mail"] in res.text:
        return {"e_mail":"already used"}
    else:
        db.save(info_user)


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
    url = 'http://admin:kolea21342@localhost:5984/captcha_test'
    random_string = a + b + c + d + f + g + h
    captcha_value = json.dumps(random_string)
    print(captcha_value)
    json_object = {"captcha_value":str(captcha_value)}
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/captcha_test')
    db.save(json_object)
    random_source = random_string + '.png'
    image = ImageCaptcha(width=100, height=90)
    gen = image.generate_image(random_string)
    gen_1 = gen.save(random_source)
    return _responses.FileResponse(random_source)


@api.post('/sessions')
async def sessions(user_session: sessions):
    user_session = user_session.dict()
    url_db = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_users/_design/design_users/_view/login?key=' + '"' + user_session['e_mail'] + '"'
    res = requests.get(url_db)
    doc = res.json()
    db = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/sessions')
    document = {
        "e_mail": user_session['e_mail'],
        "token": user_session['token'],
        "password": user_session['password'],
        "country": doc['rows'][1]['value']['country'],
        "age": doc['rows'][1]['value']['age'],
        "gender": doc['rows'][1]['value']['gender']
    }
    db.save(document)
    if db.save(document):
        return {"Session":"created"}
    else:
        return {'Status':'not done'}



@api.post('/loginn')
async def log_in(info_login: UserLogin):
    info_login = info_login.dict()
    url = 'http://admin:kolea21342@localhost:5984/reviewin_users/_design/design_users/_view/login?key=' + '"' + info_login['e_mail'] + '"'
    res = requests.get(url)
    document = res.text
    print(document)
    doc = res.json()
    if info_login['e_mail'] in document and info_login['password'] == doc['rows'][0]['value']['password']:
        return {"User":"exists"}
    else:
        return {"Status":"Not done"}



if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 2223)

