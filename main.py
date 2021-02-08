import uvicorn
from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI


app = FastAPI()

class Package(BaseModel):
    name:str
    number:str
    description : Optional[str]=None

class PackageIn(BaseModel):
    secret_id:int
    name:str
    number:str
    description : Optional[str]=None


@app.get("/")
def read_root():
    return "Hello World!!!!!!!!!!!!!!!!!!!!!!!!"


@app.get("/items/{item_id}")
def read_item(item_id):
    return {item_id}


@app.get("/component/")
async def read_component(number:int,text:str):
    return {"Number":number,"Text":text}


#@app.post("/package/{priority}")
#async def make_package(priority:int ,package:Package,value:bool):
#    return {"priority":priority,**package.dict(),"value":value}


@app.post("/package/",response_model=Package,response_model_exclude={"description"})
async def make_package(package:PackageIn):
    return package


if __name__=="__main__":
    uvicorn.run(app,port=5001)
