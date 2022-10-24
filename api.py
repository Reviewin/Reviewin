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

class logout(BaseModel):
    e_mail: str

class sessions(BaseModel):
    e_mail: str
    country: str
    age: str
    gender: str
    token: str


class UserLogin(BaseModel):
    e_mail: str
    password: str


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

@api.post('/reviewin_users')
async def sign_up(info__: User_register):
    info__ = info__.dict()
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/reviewin_users')
    if len(info__['password']) > 8 and info__['points'] == 0:
        print("User registered")
        db.save(info__)
    else:
        {"Status":"Not done"}


@api.post('/verify_user')
async def verify_user(user_verif :user__):
    user_verif = user_verif.dict()
    user_e_mail = user_verif['e_mail']
    url = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_users/_design/design_users/_view/Users?key=' + '"' + user_e_mail + '"'
    res = requests.get(url)
    print(url)
    print(res.text)
    if str(user_e_mail) in res.text:
        print('User exists')
        return {"User":"exists"}
    else:
        return {"User":'no longer exists'}


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

@api.post('/user')
async def signup(info_ :User_register):
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/reviewin_users')
    info_ = info_.dict()
    db.save(info_)
    if db.save(info_):
        return {"User":"registered"}

@api.post('/log-in')
async def signin(info_login: UserLogin):
    info_login = info_login.dict()
    info_e_mail = info_login['e_mail']
    info_password = info_login['password']
    url = 'http://admin:kolea21342@127.0.0.1:2222/reviewin_users/_design/design_users/_view/login?key=' + "%22\%22" + info_e_mail + "\%22%22"
    res = requests.get(url)
    print(res.json())
    doc = res.json()
    if info_e_mail in res.json() and info_password in res.json():
        return {"User":"exists"}
    else:
        return {"Invalid":"password or e-mail"}



@api.post('/check_captcha_value')
async def test(captcha: recaptcha):
    captcha = captcha.dict()
    url = 'http://admin:kolea21342@localhost:5984/captcha_test/_design/Captchadoc/_view/captcha_test?key='+'"'+str(captcha['captcha_value'])+'"' 
    res = requests.get(url)
    if captcha['captcha'] in res.json():
        return {"Status":"Done"}
    else:
        return {"Status":"Not Done"}
'"'
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
    if info_user["e_mail"] in res.text:
        return {"e_mail":"already used"}
    else:
        db.save(info_user)

@api.post('/verification_user')
async def verification(verification_: verification):
    verification_ = verification.dict()
    if verification_['e_mail'] in requests.get('http://admin:kolea21342@localhost:5984/reviewin_users/_all_docs?include_docs=true').text:
        return {"User":"exists"}
    else:
        return {"User":"No longer exists"}


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
    user_sessions = user_sessions.dict()
    ac  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','10','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a = _random.choice(ac)
    b = _random.choice(ac)
    c = _random.choice(ac)
    d = _random.choice(ac)
    f = _random.choice(ac)
    g = _random.choice(ac)
    h = _random.choice(ac)
    token = a + b + c + d + f + g + h
    db = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/sessions')
    doc_json = {'e_mail':user_sessions['e_mail'],'age':user_sessions['age'], 'country':user_sessions['country'], 'gender':user_sessions['gender']}
    db.save(doc_json)
    return {doc_json}

@api.post('/logout')
async def logout(log_out: logout):
    log_out = log_out.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/sessionsview?key='+'"'+ log_out['e_mail'] + '"'
    res = requests.get(url)
    doc = res.json()
    doc_id = doc['rows'][1]['id']
    url_document = 'http://admin:kolea21342@127.0.0.1:5984/sessions/' + doc_id
    if __name__ == '__main__':
        res = requests.delete(url_document)
        return {"Session":"deleted"}
    else:
        return {"Session":"failed to delete"}


@api.get('/text')
def tt():
    return {"True"}

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

@api.post('/signin')
async def sign_in(info_login: UserLogin):
    info_login = info_login.dict()
    url = 'http://admin:kolea21342@localhost:5984/reviewin_users/_all_docs?include_docs=true'
    res = requests.get(url)
    if str(info_login['e_mail']) and str(info_login['password']) in res.text:
        return {"Status":"Done"}
    else:
        print("it doesn't work")
        return {"Status":"Not done"}

@api.post('/endpoint')
def test():
    return {"test":"done"}

@api.post('/log-in')
async def log_in(info_login: UserLogin):
    info_login = info_login.dict()
    url = 'http://admin:kolea21342@localhost:5984/reviewin_users/_design/design_users/_view/login?key=' + '"' + info_login['e_mail'] + '"'
    res = requests.get(url)
    doc = res.json()
    password = doc['rows'][1]['value']['password']
    e_mail = doc['rows'][1]['key']
    if info_login['e_mail'] != e_mail or info_login['password'] != password:
        return {'Status':'Not done'}
    elif info_login['e_mail'] not in res.json():
        return {"User":"no longer exists"}
    else:
        return {"User":"exists"}
@api.get('/get')
async def get():
    return {'True'}

if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 2222)
