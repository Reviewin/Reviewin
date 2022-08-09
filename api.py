from fastapi import FastAPI 
import uvicorn
from typing import Union
from pydantic import BaseModel
from typing import Optional
import couchdb

api = FastAPI() #on instancie 


class User_register(BaseModel):
    first_name: str
    last_name: str
    gender: str
    age: str
    address: str
    e_mail: str




@api.post('/users') 
async def sign_up_user(info_user: User_register):
    couch_server = couchdb.Server("http://admin:kolea21342@localhost:5984/")
    couch_db = couch_server.create("my_database_2")
    couch_db.save(info_user.dict())
    return {"Status":"Done"}



if __name__ == '__main__':
    uvicorn.run(api, host= '127.0.0.1', port= 8000)
