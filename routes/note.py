from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

note = APIRouter()

#note.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def home(request: Request):
    docs = conn.cllg.bachhe.find({})
    newDoc = []
    for doc in docs:
        newDoc.append({
            "id" : doc["_id"],
            "title" : doc["title"],
            "desc" : doc["desc"],
            "important" : doc["important"]
        })
    return templates.TemplateResponse(
       "index.html",{ "request":request, "newDoc": newDoc}
    )




@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    print(form)
    formDict = dict(form)
    formDict["important"] = True if formDict["important"] =="on" else False
    note = conn.cllg.bachhe.insert_one(formDict)
    return {"success" : True}
    # inserted_note = conn.cllg.bachhe.insert_one(dict(note))
    # return noteEntity(inserted_note)
    