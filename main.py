from fastapi import FastAPI
import json

def loadData():
    with open('patient.json','r',encoding="utf-8") as f:
        data=json.load(f)
    return data

app = FastAPI()

@app.get("/")  # 1st route define 
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about') #2nd route 
def about():
    return {'message':'Here we design fully functional API for your Patient Records Managemnt'}

@app.get('/view')
def view():
    data = loadData()
    return data