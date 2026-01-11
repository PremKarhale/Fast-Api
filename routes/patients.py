from fastapi import APIRouter
from fastapi import FastAPI,Path,HTTPException
from typing import Optional
import json 

def loadData():
    with open('patient.json','r',encoding="utf-8") as f:
        data=json.load(f)
    return data

router=APIRouter(
    prefix="/patient",
    tags=["patients"]
)

# Added path parameter 
@router.get('/{patient_id}')
def view_patient(patient_id:str=Path(...,description='ID of patient in a Database',example='P001')):
    data=loadData() #load all data
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient details not Found...') # if data comes then show it else raise an http exception error 