from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def route():
    return {"teasst":"tessxt"}

@app.get('/t')
def route_t():
    return {"teasst":"tessdwadxtse"}