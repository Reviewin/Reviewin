from fastapi import FastAPI, UploadFile, File, responses, Form
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
import aiofiles
import os
from services import services
import uuid
import regex as re
import services
from services import final_list_of_countries_imported_uwu
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



#ajout de produit, on passe les informations dans le corps de la requete puis on enregitre le produit dans la db  
@api.post("/products")
async def create_upload_file(company: str = Form(),type_of_products: str =  Form(),informations: str = Form(),file: UploadFile = File(...)):
    random_id = str(uuid.uuid4()) + '.png'
    file.filename = str(random_ide)
    #données à envoyer à la db 
    payload = {
        "type_of_products":json.dumps(type_of_products).replace('"',''),
        "company":json.dumps(company).replace('"',''),
        "informations":json.dumps(informations).replace('"',''),
        "product_id":str(random_id).replace('.png', '')
    }
    print(payload)
    database = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/reviewin_products')
    database.save(payload)
    file_location = f"C:/Users/33769/Desktop/Reviewin/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}

# acquérir les données selon un certain produit
@api.post('/products/informations')
async def return_informations(product_informations: Product_informations):
    product_informations = product_informations.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_products/_design/product_desogn/_view/product_view?key="' + str(product_informations['product_id']) + '"'
    url_verif = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loadddatas?key="' + str(product_informations['token']) + '"'
    response = requests.get(url_verif)
    doc = response.json()
    if product_informations['token'] in doc:
        res = requests.get(url)
        return {"Informations":res.json()}
    else:
        return {"Status":"not done"}
# pas encore opérationnel
@api.post('/notations')
async def notations(notations: notations):
    notations = notations.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loadddatas?key="' + notations['token'] + '"'
    url_for_notations = 'http://admin:kolea21342@127.0.0.1:5984/products_notations/_design/design_notations/_view/view_notations?key="' + notations['product_id'] + '"'
    database = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/product_notations')
    payload = {
        'product_id':notations['product_id'],
        "email":notations['e_mail'],
        "age":notations['age'],
        "gender":notations['gender'],
        "country":notations['country']
        
    }
    if notations['token'] in requests.get(url).json():
        if notations['e_mail'] not in requests.get(url_for_notations).json():
            print('update number of points')
            return {"Status":"Done"}
            #update le nombre de points dans la db users
        else:
            print('user already reviewed')
            return {"Status":"Not done"}
    else:
        return {"User":"Not connected"}

#pas encore opérationnel
@api.post('/load_comments')
async def load_comments(com: com):
    com = com.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key="' + com['token'] + '"'
    url_view_products = 'http://admin:kolea21342@127.0.0.1:5984/products_notations/_design/design_notations/_view/comments?key="' + com['product_id'] + '"'
    response = requests.get(url)
    list_of_comments = []
    if com['token'] in response.text:
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
        print("no")

#supprimer un produit (pas encore de test coté db)
@api.post('/delete')
async def delete_products(partners: products_delete):
    partners = partners.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loadddatas?key="' + partners['token'] + '"'
    a = partners['token']
    response = requests.get(url)
    path = 'C:/Users/33769/Desktop/Reviewin'
    path_2 = str(path + partners['partner_product_id'])
    database = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/products')
    #création d'une vue pour récupérer l'id du document selon l'id du produit demandé.
    # url vue: 
    # requete vue
    # doc = requetevue.json() 
    os.listdir(path)
    if a in response.json():
        if partners['partner_product'] in os.listdir(path):
            os.remove(path_2)
        else:
            return {"Product_id":"Not Valid"}
    else:
        return {"Status":"Not done"}
#acquérir l'image d'un produit selon un id
@api.get('/products/{id}')
async def get_produtcts(id: str ):
    image = str(id) + '.png'
    return _responses.FileResponse(image)

#ancienne_fonction
@api.get('/products')
async def list_products():
    path = "C:/Users/33769/Desktop/Reviewin"
    valid_extension = '.png'
    files = os.listdir(path)
    list_of_products = []
    valid_extension = '.png'
    for i in range(len(files)):
        if files[i].endswith(valid_extension):
            list_of_products.append(files[i])
    print(list_of_products)
    return list_of_products

#recevoir la liste des produits, d'abord une vérification que l'utilisateur est connecté, puis renvoyé une liste []
@api.post('/products/list')
async def list_products(products: condition_products):
    products = products.dict()
    path = "C:/Users/33769/Desktop/Reviewin"
    valid_extension = '.png'
    files = os.listdir(path)
    list_of_products = []
    valid_extension = '.png'
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key=' + '"' + products['token'] + '"' 
    res = requests.get(url)
    doc = res.json()
    print(res.text)
    print(products['token'])
    if doc['rows'][0]['key'] == products['token']:
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


@api.post('/reviewin_users')
async def sign_up(info__: User_register):
    info__ = info__.dict()
    user_e_mail = info__['e_mail']
    url = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_users/_design/design_users/_view/Users?key=' + '"' + user_e_mail + '"'
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/reviewin_users')
    res = requests.get(url)
    gender_list = ['M', 'F']

    if user_e_mail not in res.json():
        if len(info__['password']) > 8 and info__['points'] == 0 and info__['gender'] in gender_list and len(info__['country']) > 3 and int(info__['age'] >= 16):
            print("User registered")
            db.save(info__)
            return {"User":"Saved"}
        else:
            return {"Password":"Not valid"}
    else:
        return {"Status":"Not done"}


@api.post('/logout')
async def logout(logout_: logoutf):
    logout_ = logout_.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key=' + '"' + logout_['token'] + '"'
    url_ = "http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key=%22" + logout_['token'] + '%22'
    response = requests.get(url_)
    doc = response.json()
    print(doc)
    id_ = doc['rows'][0]['id']
    couch = couchdb.Server('http://admin:kolea21342@127.0.0.1:5984/')
    db = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/sessions/')
    db.delete(db[str(id_)])
    return {"Status":"Done"} 


@api.post('/accounts')
async def verify_captcha_test(captcha: Recaptcha_2):
    captcha = captcha.dict()
    captcha_value = captcha['captcha_value']
    url = 'http://admin:kolea21342@127.0.0.1:5984/captcha_test/_design/Captchadoc/_view/captcha_test?key=' + "%22\%22" + captcha_value + "\%22%22"
    database = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/captcha_test/')
    ma_variable = requests.get(url)
    user_e_mail = captcha['email']
    url_e_mail = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_users/_design/design_users/_view/Users?key="'+ user_e_mail + '"'
    resp = requests.get(url_e_mail)
    payload = {
        "age":captcha['age'],
        "country":captcha['country'],
        "email":captcha['email'],
        "gender":captcha['gender'],
        "password":captcha['password'],
        "points":captcha['points'],
    }
    database_reviewin_users = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/reviewin_users')
    pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    list_of_genders = ['M', 'F']
    doc = resp.json()
    document = ma_variable.json()
    if captcha_value in ma_variable.text:
        print('Valid Captcha')
        if re.search(pattern, captcha['email']) and int(captcha['age']) >= 16 and len(captcha['password']) and captcha['points'] == 0 and str(captcha['gender']) in list_of_genders and captcha['country'].upper() in final_list_of_countries_imported_uwu:
            if user_e_mail not in resp.text:
                print(resp.json())
                database_reviewin_users.save(payload)
                captcha_file = str(captcha['captcha_value']) + '.png'
                os.remove(captcha_file)
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

@api.post('/signup')
async def signup(User: User):
    User = User.dict()
    captcha_value = User['recaptcha_value']
    url = 'http://admin:kolea21342@127.0.0.1:5984/captcha_test/_design/Captchadoc/_view/captcha_test?key=' + "%22\%22" + captcha_value + "\%22%22"
    user_e_mail = User['email']
    url_e_mail = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_users/_design/design_users/_view/Users?key=' + '"' + user_e_mail + '"'
    resp = requests.get(url)
    database = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/reviewin_users')
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

@api.post('/load')
async def load_(load_data: load_):
    load_data = load_data.dict()
    url = 'http://admin:kolea21342@127.0.0.1:5984/sessions/_design/sessions/_view/loaddatas?key="'+ load_data['token'] + '"'
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
    image = ImageCaptcha(width=600, height=400)
    gen = image.generate_image(random_string)
    gen_1 = gen.save(random_source)
    return _responses.FileResponse(random_source)


@api.post('/sessions')
async def sessions(user_session: sessions):
    user_session = user_session.dict()
    url_db = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_users/_design/design_users/_view/login?key="'+ user_session['e_mail'] + '"'
    res = requests.get(url_db)
    document_ = res.json()
    print(document_)
    print(res.text)
    doc = res.text
    db = couchdb.Database('http://admin:kolea21342@127.0.0.1:5984/sessions')
    document = {
        "e_mail": user_session['e_mail'],
        "token": user_session['token'],
        "password": user_session['password'],
        "country": document_['rows'][0]['value']['country'],
        "age": document_['rows'][0]['value']['age'],
        "gender": document_['rows'][0]['value']['gender']
    }
    if user_session['e_mail'] in doc and user_session['password'] in doc:
        db.save(document)
        return {"Session":"created"}
    else:
        return {"Session":"not created"}
    #db.save(document)
    #return {"Session":"created"}


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
