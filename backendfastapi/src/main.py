from fastapi import FastAPI
from decouple import config
from contextlib import asynccontextmanager
from api.db import db_init
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app:FastAPI):

    db_init()
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chat")

API_KEY = config("API_KEY")
if not API_KEY:
    raise NotImplementedError("api key is not implemeanted")

@app.get('/')
def route():
    return {"teasst":"tessxt"}

@app.get('/t')
def route_t():
    return {"teasst":"tessdwadxtse"}