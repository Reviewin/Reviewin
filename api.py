from fastapi import FastAPI, Body 
import uvicorn
from typing import Union
from pydantic import BaseModel
from typing import Optional
import couchdb
from couchdb import Server


api = FastAPI() #on instancie 

class User_register(BaseModel):
    first_name: str
    last_name: str
    gender: str
    age: int
    address:str 
    e_mail:  str



@api.on_event("/startup/")
async def startup_event():
    couch_server = couchdb.Server("http://admin:kolea21342@localhost:5984/")
    couch_database = couch_server.create('db_reviewin_real')



@api.post('/postuserinfo')
def create_post(payload: dict = Body(...):
    couch_server = couchdb.Server('http://admin:kolea21342@localhost:5984/')
    couch_data = couch_server.create('db_this_user')
    couch_data.save(payload)
    return {"Status":"Done"}  


if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 8000)
