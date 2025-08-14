from typing import Union

from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://naharkeshav1212:keshav2003@cluster0.7tostpi.mongodb.net/cllg")




@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    docs = conn.cllg.bachhe.find({})
    newDoc = []
    for doc in docs:
        newDoc.append({
            "id" : doc["_id"],
            "name" : doc["name"],
            "rno" : doc["rno"]
        })
    return templates.TemplateResponse(
       "index.html",{ "request":request, "newDoc": newDoc}
    )


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/desc")
def get_desc():
    return {"hello i am keshav"}