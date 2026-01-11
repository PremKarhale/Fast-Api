import json
from fastapi import APIRouter

def loadData():
    with open('patient.json','r',encoding="utf-8") as f:
        data=json.load(f)
    return data

router=APIRouter(
    prefix='/view',
    tags=["View"]
)

#Data of all the patients 
@router.get('')
def view():
    data = loadData()
    return data
