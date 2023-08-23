import os
import aiofiles
import shutil

import random
import uuid
import regex as re

import json
from PIL import Image

import requests

import uvicorn

import subprocess

from fastapi import FastAPI, File, Form, Request, responses, UploadFile
import fastapi.responses as _responses
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel

from typing import Union
from typing import Optional

import couchdb

from starlette.middleware.base import BaseHTTPMiddleware

import captcha 
from captcha.image import ImageCaptcha

import bcrypt

import hashlib

import passlib
from passlib.hash import pbkdf2_sha256 as sh

import ipaddress

api = FastAPI() #on instancie 

#ici nous avons majoritairement les modèles de données qui nous servirons plus tard

class logout(BaseModel):
    e_mail: str

class sessions(BaseModel):
    e_mail: str
    password: str
    token: str

class UserLogin(BaseModel):
    e_mail: str
    password: str
    token: str

class logoutf(BaseModel):
    token: str

class load_(BaseModel):
    token: str

class User_register(BaseModel):
    gender: str
    age: int
    country: str
    e_mail: str
    password: str
    points: int

class recaptcha(BaseModel):
    captcha_value:  str

class User(BaseModel):
    gender: str
    age: str
    country: str
    email: str
    password: str
    points: int
    recaptcha_value: str

class verification(BaseModel):
    e_mail: str
    age: str
    gender: str
    password: str
    country: str

class user__(BaseModel):
    e_mail: str

class Recaptcha_2(BaseModel):
    gender: str
    age: str
    country: str
    email: str 
    password: str
    points: int
    captcha_value: str

class condition_products(BaseModel):
    token: str

class products_delete(BaseModel):
    token: str
    partner_product: str

class notations(BaseModel):
    token:str
    e_mail: str
    age: str
    interactions: str
    gender: str
    country: str
    product_id: str
    comments: str
    number_of_points: int

class opinions(BaseModel):
    e_mail:str
    age: str
    country:str
    product_id: int
    gender: str
    token: str
    opinion: str

class Product_informations(BaseModel):
    token: str 
    product_id: int
    
class Products(BaseModel):
    type_of_products: str
    company: str

class ProductsDatabases(BaseModel):
    type_of_products: str
    company: str

class test(BaseModel):
    test: str

class com(BaseModel):
    token: str
    product_id: str 


class AdminRegister(BaseModel):
    password: str
    email: str
    name_company: str
    phone_number: str
    address: str
    nationality: str
    type_of_company: str
    description: str
    contract: str

import importlib.util
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)

#ajout de produit, on passe les informations dans le corps de la requete puis on enregitre le produit dans la db  
@api.post("/products", tags=["Products verification"])
async def create_upload_file(company: str = Form(),type_of_products: str =  Form(),informations: str = Form(),file: UploadFile = File(...), token: str = Form()):
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loadddatas?key="{token}"'
    response = requests.get(url)
    doc = response.json()
    import imghdr
    valid_formats = ['bmp', 'jpeg', 'png', 'svg']
    def not_empty(string:str) -> bool:
        if len(string) != 0:
            return True
        else:
            return False
    if not_empty(str(company)) and not_empty(str(type_of_products)) and not_empty(str(informations)) and doc['rows'][0]['key'] == "partner" and doc['rows'][0]['value'] == token:
        if imghdr.what(None, h=file.file.read()) in valid_formats:
            print(imghdr.what(None, h=file.file.read()))
            random_id = str(uuid.uuid4()) + '.png'
            file.filename = str(random_id)
            #données à envoyer à la db
            try:
                import datetime
            except ModuleNotFoundError as m:
                return False 
            payload = {
                "type_of_products":json.dumps(type_of_products).replace('"',''),
                "company":json.dumps(company).replace('"',''),
                "informations":json.dumps(informations).replace('"',''),
                "product_id":str(random_id).replace('.png', ''),
                "year": datetime.datetime.now().year,
                "day":datetime.datetime.now().day,
                "hour":datetime.datetime.now().hour,
                "minute":datetime.datetime.now().minute,
                "second":datetime.datetime.now().second
            }
            print(payload)
            database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_products')
            database.save(payload)
            file_location = f"C:/Users/33769/Desktop/Images_Captcha/{file.filename}"
            valid_formats = ['bmp', 'jpeg', 'png', 'svg']
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            return {"info": f"file '{file.filename}' saved at '{file_location}'"}
        else:
            return {"Bad":"format"}
    else:
        return {"Status":"not done"}

# acquérir les données selon un certain produit
@api.post('/products/informations',tags=['Endpoints of user display informations'])
async def return_informations(product_informations: Product_informations):
    product_informations = product_informations.dict()
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_products/_design/product_desogn/_view/product_view?key="' + str(product_informations['product_id']) + '"'
    url_verif = f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loadddatas?key="' + str(product_informations['token']) + '"'
    response = requests.get(url_verif)
    doc = response.json()
    if sh.hash(product_informations['token']) in doc:
        res = requests.get(url)
        return {"Informations":res.json()}
    else:
        return {"Status":"not done"}
# pas encore opérationnel
@api.post('/notations', tags=['Notations'])
async def notations(notations: notations):
    notations = notations.dict()
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loadddatas?key="' + notations['token'] + '"'
    url_for_notations = f'http://{module.username}:{module.password}@127.0.0.1:5984/products_notations/_design/design_notations/_view/view_notations?key="' + notations['product_id'] + '"'
    database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/product_notations')
    payload = {
        'product_id':notations['product_id'],
        "email":notations['e_mail'],
        "age":notations['age'],
        "gender":notations['gender'],
        "country":notations['country'],
        "year": datetime.datetime.now().year,
        "day":datetime.datetime.now().day,
        "hour":datetime.datetime.now().hour,
        "minute":datetime.datetime.now().minute,
        "second":datetime.datetime.now().second
    }
    if notations['token'] in requests.get(url).json():
        if notations['e_mail'] not in requests.get(url_for_notations).json():
            #update le nombre de points dans la db users
            print('update number of points')
            response = requests.get(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users/_design/design_users/_view/update-points?key="{notations["email"]}"')
            database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users')
            id = response.json()['rows'][0]["id"]
            document = database[id]
            key = "points"
            document[key] = document[key] + 5
            database[id] = document
            return {"Status":"Done"}
        else:
            print('user already reviewed')
            return {"Status":"Not done"}
    else:
        return {"User":"Not connected"}

#pas encore opérationnel
@api.post('/load_comments', tags=['Endpoints of user display informations'])
async def load_comments(com: com):
    com = com.dict()
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key="' + com['token'] + '"'
    url_view_products = f'http://{module.username}:{module.password}@127.0.0.1:5984/products_notations/_design/design_notations/_view/comments?key="' + com['product_id'] + '"'
    response = requests.get(url)
    list_of_comments = []
    if sh.hash(com['token']) in response.text:
        res = requests.get(url_view_products)
        print(res.json())
        doc = res.json()
        print(len(doc['rows']))
        list_of_comments = []
        for i in range(len(doc['rows'])):
            list_of_comments.append(doc['rows'][i]['value'])
        print(list_of_comments)
        return list_of_comments
    else:
        return {"Status":"Not done"}

#supprimer un produit (pas encore de test coté db)
@api.post('/delete', tags=["Delete a product from app"])
async def delete_products(partners: products_delete):
    partners = partners.dict()
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loadddatas?key="' + partners['token'] + '"'
    token = partners['token']
    response = requests.get(url)
    product_id = partners['product_id']
    path = f'C:/Users/33769/Desktop/Images_Captcha/{product_id}.png'
    response = requests.get(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_products/_design/product_design/_view/product-delete/key="{product_id}"')
    database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_products')
    document = response.json()
    id = document['rows'][0]["value"]
    #création d'une vue pour récupérer l'id du document selon l'id du produit demandé.
    # url vue: 
    # requete vue
    # doc = requetevue.json() 
    os.listdir(path)
    if token in response.json():
        if partners['partner_product'] in os.listdir(path):
            os.remove(path_2)
            database.delete(database[str(id)])
            if database.delete(database[str(id)]):
                return {"Status":"Done"}
        else:
            return {"Product_id":"Not Valid"}
    else:
        return {"Status":"Not done"}
#acquérir l'image d'un produit selon un id
@api.get('/products/{id}')
async def get_produtcts(id: str ):
    image = f"C:/Users/33769/Desktop/Images_Captcha/" + str(id).replace('"', '') + ".png"
    return _responses.FileResponse(image)

#ancienne_fonction
@api.get('/products', tags=["Old endpoint"])
async def list_products():
    path = "C:/Users/33769/Desktop/Reviewin/api-server-fastapi"
    valid_extension = '.png'
    files = os.listdir(path)
    list_of_products = []
    valid_extension = '.png'
    for i in range(len(files)):
        if files[i].endswith(valid_extension):
            list_of_products.append(files[i].replace('.png', ''))
    print(list_of_products)
    return list_of_products

#recevoir la liste des produits, d'abord une vérification que l'utilisateur est connecté, puis renvoyé une liste []
@api.post('/products/list', tags=['Get the products'])
async def list_products(products: condition_products):
    products = products.dict()
    path = "C:/Users/33769/Desktop/Reviewin"
    valid_extension = '.png'
    files = os.listdir(path)
    list_of_products = []
    valid_extension = '.png'
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key="'+ str(products['token']) + '"'
    res = requests.get(url)
    doc = res.json()
    print(res.text)
    print(products['token'])
    print(doc)
    if doc['rows'][0]['key'] == sh.hash(products['token']):
        print("Successfull")
        for i in range(len(files)):
            if files[i].endswith(valid_extension):
                list_of_products.append(files[i])
        print(list_of_products)
        return list_of_products
    elif len(doc['rows']) == 0:
        return {"False"}
    else:
        return {"Status":"Not Done"}

@api.post('/reviewin_users', tags=["Old endpoint"])
async def sign_up(info__: User_register):
    info__ = info__.dict()
    user_e_mail = info__['e_mail']
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users/_design/design_users/_view/Users?key=' + '"' + user_e_mail + '"'
    db = couchdb.Database(f'http://{module.username}:{module.password}@localhost:5984/reviewin_users')
    res = requests.get(url)
    gender_list = ['M', 'F']
    password_hash = sh.hash(info__['password'])
    info__['password'] = password_hash #je stocke le hash sous forme hexadécimale pour par lasuite comparer que les hash en hexadécimales lors des notations et autres intéractions
    if user_e_mail not in res.json():
        if len(info__['password']) > 8 and info__['points'] == 0 and info__['gender'] in gender_list and len(info__['country']) > 3 and int(info__['age'] >= 16):
            print("User registered")
            db.save(info__)
            return {"User":"Saved"}
        else:
            return {"Password":"Not valid"}
    else:
        return {"Status":"Not done"}

@api.post('/logout', tags=['Sessions'])
async def logout(logout_: logoutf):
    logout_ = logout_.dict()
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key=' + '"' + logout_['token'] + '"'
    url_ = f"http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key=%22" + logout_['token'] + '%22'
    response = requests.get(url_)
    doc = response.json()
    print(doc)
    id_ = doc['rows'][0]['id']
    couch = couchdb.Server(f'http://{module.username}:{module.password}@127.0.0.1:5984/')
    db = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/')
    db.delete(db[str(id_)])
    return {"Status":"Done"} 

#sign-up officiel les autres endpoints ne sont que des crash tests
@api.post('/accounts', tags=["Create Account"])
async def verify_captcha_test(captcha: Recaptcha_2, request: Request):
    import validate_email
    from validate_email import validate_email
    import datetime
    captcha = captcha.dict()
    captcha_value = captcha['captcha_value']
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/captcha_test/_design/Captchadoc/_view/captcha_test?key="{captcha_value}"' 
    database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/captcha_test/')
    ma_variable = requests.get(url)
    user_e_mail = captcha['email']
    url_e_mail = f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users/_design/design_users/_view/Users?key="{user_e_mail}"'
    resp = requests.get(url_e_mail)
    payload = {
        "role":"consumer",
        "age":captcha['age'],
        "country":captcha['country'],
        "email":captcha['email'],
        "gender":captcha['gender'],
        "password":sh.hash(str(captcha['password'])), #on hashe le mot de passe 
        "client": str(request.headers.get("User-Agent")),
        "ip": sh.hash(str(request.headers.get("X-Forwarded-For", request.client.host))),
        "points":captcha['points'],
        "language":str(request.headers.get("accept-language"[0:2])),
        "year":datetime.datetime.now().year,
        "day":datetime.datetime.now().day,
        "hour":datetime.datetime.now().hour,
        "minute":datetime.datetime.now().minute
    }
    database_reviewin_users = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users')
    pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    list_of_genders = ['M', 'F']
    doc = resp.json()
    document = ma_variable.json()
    def valid_ip(ip)->bool:
        import ipaddress
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False
    def check_server_mail(list_domain: list) -> bool:
        import smtplib
        list_domains_available = []
        try:
            for i in range(len(list_domain)):
                with smtplib.SMTP(list_domain[i]) as smtp:
                    list_domains_available.append(list_domain[i])
            if len(list_domain) == len(list_domains_available):
                return True
            else:
                return False
        except(smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected):
            return False
    def check_mx_records(domain: str)-> bool or list:
        import dns.resolver
        mx = [] 
        try:
            responses = dns.resolver.resolve(domain, 'MX')
            mx = [str(r.exchange)[:-1] for r in responses]
            print(mx)
            return mx
        except dns.resolver.NoAnswer:
            return False
    def _list_countries()->list:
        import random 
        import pycountry
        from pycountry import countries
        final_list_of_countries_imported_uwu = []
        for i in range(len(pycountry.countries)):
            final_list_of_countries_imported_uwu.append(list(pycountry.countries)[i].name.upper())
        return final_list_of_countries_imported_uwu
    domain = captcha["email"].split("@")[1]
    print(resp.json())
    country_upper = captcha["country"].upper()
    print(validate_email(captcha['email']))
    print(len(check_mx_records(domain)) > 0)
    print(check_server_mail(check_mx_records(domain)))
    print(country_upper in _list_countries())
    if captcha_value in ma_variable.text:
        print('Valid Captcha')
        if validate_email(captcha['email']) and int(captcha['age']) >= 16 and len(captcha['password']) >=8 and captcha['points'] == 0 and str(captcha['gender']) in list_of_genders and len(check_mx_records(domain)) > 0 and check_server_mail(check_mx_records(domain)) and country_upper in _list_countries():
            if user_e_mail not in resp.text and sh.hash(payload["ip"]) not in resp.text:
                print(resp.json())
                database_reviewin_users.save(payload)
                captcha_file = str(captcha['captcha_value']) + '.png'
                os.remove(f"C:/Users/33769/Desktop/Images_Captcha/{captcha_file}")
                id_ = document['rows'][0]['id']
                database.delete(database[str(id_)])
                return {"Captcha":"good let sign up"}
            else:
                return {"User":"already exists"}
        else:
            return {"Syntax or informations":"Invalid"}
    else:
        print('Invalid captcha')
        return {"Not good captcha":"don't let sign up"}

@api.post('/signup', tags=["Old endpoint"])
async def signup(User: User):
    User = User.dict()
    captcha_value = User['recaptcha_value']
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/captcha_test/_design/Captchadoc/_view/captcha_test?key=' + "%22\%22" + captcha_value + "\%22%22"
    user_e_mail = User['email']
    url_e_mail = f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users/_design/design_users/_view/Users?key=' + '"' + user_e_mail + '"'
    resp = requests.get(url)
    database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users')
    response = requests.get(url_e_mail)
    payload = {
        "age":User['age'],
        "country":User['country'],
        "email":User['email'],
        "gender":User['gender'],
        "password":User['password'],
        "points":User['points'], 
    }
    if User['recaptcha_value'] in resp.json():
        print('yes')
        if user_e_mail not in response.text:
            database.save(payload)
            return {"User":"Saved"}
        else:
            return {"User":"already exists"}
    else:
        return {"Invalid":"captcha"}

@api.post('/load', tags=['Endpoints of user display informations'])
async def load_(load_data: load_):
    load_data = load_data.dict()
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key="'+ sh.hash(load_data['token'])+ '"'
    res = requests.get(url)
    doc = res.json()
    document_return = {
        "email":doc['rows'][0]['value']['e_mail'],
        "age":doc['rows'][0]['value']['age'],
        "country":doc['rows'][0]['value']['country'],
        "gender":doc['rows'][0]['value']['gender']
    }
    print(doc)
    print(doc['rows'][0]['key'])
    return document_return


@api.post('/users', tags=["Old endpoint"])
async def test_verification(info_user: User_register):
    db = couchdb.Database(f'http://{module.username}:{module.password}@localhost:5984/reviewin_users/')
    info_user = info_user.dict()
    res = requests.get(f'http://{module.username}:{module.password}@localhost:5984/reviewin_users/_all_docs?include_docs=true')
    print(res.text)
    if info_user["e_mail"] in res.text:
        return {"e_mail":"already used"}
    else:
        db.save(info_user)


@api.get('/captcha', tags=['Captcha test'])
async def return_image():
    import datetime
    ac  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','10','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a = random.choice(ac)
    b = random.choice(ac)
    c = random.choice(ac)
    d = random.choice(ac)
    f = random.choice(ac)
    g = random.choice(ac)
    h = random.choice(ac)
    url = f'http://{module.username}:{module.password}@127.0.0.1:5984/captcha_test'
    random_string = a + b + c + d + f + g + h
    captcha_value = json.dumps(random_string)
    print(captcha_value)
    json_object = {"captcha_value":random_string, "year": str(datetime.datetime.now().year),"day":str(datetime.datetime.now().day), "hour":str(datetime.datetime.now().hour), "minute":str(datetime.datetime.now().minute), "second": str(datetime.datetime.now().second)}
    db = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/captcha_test')
    db.save(json_object)
    random_source = random_string + '.png'
    image = ImageCaptcha(width=600, height=400)
    gen = image.generate_image(random_string)
    gen_1 = gen.save(f"C:/Users/33769/Desktop/Images_Captcha/{random_source}")
    return _responses.FileResponse(f'C:/Users/33769/Desktop/Images_Captcha/{random_source}')


@api.post('/sessions', tags=['Sessions'])
async def sessions(user_session: sessions):
    user_session = user_session.dict()
    url_db = f'http://{module.username}:{module.password}@127.0.0.1:5984/reviewin_users/_design/design_users/_view/login?key="'+ user_session['e_mail'] + '"'
    res = requests.get(url_db)
    document_ = res.json()
    print(document_)
    print(res.text)
    doc = res.text
    db = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions')
    document = {
        "e_mail": user_session['e_mail'],
        "token": sh.hash(user_session['token']),
        "password": user_session['password'],
        "country": document_['rows'][0]['value']['country'],
        "age": document_['rows'][0]['value']['age'],
        "gender": document_['rows'][0]['value']['gender'],
        "points":document_['rows'][0]['value']['points'],
    }
    if user_session['e_mail'] in doc and sh.hash(user_session['password']) in doc:
        db.save(document)
        return {"Session":"created"}
    else:
        return {"Session":"not created"}
    #db.save(document)
    #return {"Session":"created"}


@api.post('/loginn',tags=['Sessions'])
async def log_in(info_login: UserLogin):
    info_login = info_login.dict()
    email = info_login['e_mail']
    url = f'http://{module.username}:{module.password}@localhost:5984/reviewin_users/_design/design_users/_view/login?key="{email}"'
    res = requests.get(url)
    document = res.text
    print(document)
    doc = res.json()
    payload = {
        "e_mail":info_login['e_mail'],
        "password":sh.hash(info_login["password"]),
        "token":sh.hash(info_login['token']),
        "gender": doc["rows"][0]["value"]["gender"],
        
    }
    database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/sessions')
    if info_login['e_mail'] in document and sh.verify(info_login['password'], doc['rows'][0]['value']):
        database.save(payload)
        return {"User":"exists"}
    else:
        return {"Status":"Not done"}

@api.post("/add-admin")
async def add_admin():
    pass

@api.get("/test", tags=['Old endpoint'])
def return_test():
    return {"test":'passed'}

if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 2223)
