from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # 1st route define 
def hello():
    return {'message':'Hello World'}

@app.get('/about') #2nd route 
def about():
    return {'message':'campus X is the coding platform hosted by nitish sir '}