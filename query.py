from fastapi import FastAPI,Path,HTTPException,Query
import json

def loadData():
    with open('patient.json','r',encoding="utf-8") as f:
        data=json.load(f)
    return data

app = FastAPI()

@app.get("/")  # 1st route define 
def hello():
    return {'message':'Patient Management System'}

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

# Query parameter 

## build a query parameter of sorting the patients based on their weights and hight or bmi in ascending or descending order 

@app.get('/sort')
def sort_patient(sort_by:str=Query(...,description='Sort on the basis of height,weight or bmi '),order:str=Query('asc',description='Sort values in the asc or desc order')):
    valid_field = ['height','bmi','weight']
    if sort_by  not in  valid_field:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_field}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid field choosed , choose from asc or desc')
    
    data = loadData()
    set_order = True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by , 0) , reverse=set_order)
    return sorted_data


         