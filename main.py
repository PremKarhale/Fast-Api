from fastapi import FastAPI,Path,HTTPException
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


#Data of all the patients 
@app.get('/view')
def view():
    data = loadData()
    return data

#Data of specific patient
@app.get('/patient/{patient_id}')

# Added path parameter 
def view_patient(patient_id:str=Path(...,description='ID of patient in a Database',example='P001')):
    data=loadData() #load all data
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient details not Found...') # if data comes then show it else raise an http exception error 