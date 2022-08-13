from fastapi import FastAPI 
import uvicorn
from typing import Union
from pydantic import BaseModel
from typing import Optional
import couchdb
import requests
import json



api = FastAPI() #on instancie 


class User_register(BaseModel):
    first_name: str
    last_name: str
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


@api.post('/test_verification')
async def test_verification(info_user: User_register):
    db = couchdb.Database('http://admin:kolea21342@localhost:5984/my_database_2')
    info_user = info_user.dict()
    if len(info_user["password"]) < 8:
        return {"bad":"password"}
    else:
        db.save(info_user)
        return {"Status":"Done"}

@api.get('/login')
async def login_user():
    return {"Hello":"World"}


if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 2222)
