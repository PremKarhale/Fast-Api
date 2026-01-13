from fastapi import APIRouter 
from fastapi import FastAPI,Path,HTTPException 
from fastapi.responses import JSONResponse
from schemas import Patient
import json 


# UTILITY FUNCTIONS
def loadData():
    with open('patient.json','r',encoding="utf-8") as f:
        data=json.load(f)
    return data

def saveData(data):
    with open('patient.json','w') as f:
        json.dump(data,f)


router=APIRouter(
    prefix="/patient",
    tags=["patients"]
)

#Get : Data of all the patients
@router.get("/view")
def view():
    data = loadData()
    return data


#Get :Data of Single Patient
@router.get("/view/{patient_id}")
def view_patient(patient_id:str=Path(...,description='ID of patient in a Database',example='P001')):
    data=loadData() #load all data
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient details not Found...') # if data comes then show it else raise an http exception error 

#Post route
@router.post('/create')
def create_patient(patient:Patient):
    #load existing data
    data = loadData()

    # check wheather the patient ID already exist in the data
    if patient.id in data:
        raise HTTPException (status_code=400 , detail="Patient already exist")
    
    # add new Patient 
    data[patient.id]=patient.model_dump(exclude=['id']) # converts from pydentic obj to dictonary
    
    # save the data into patient.json 
    saveData(data)

    return JSONResponse(status_code=201, content={"message":"Patinet added Successfully !!"})
