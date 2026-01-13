from fastapi import APIRouter 
from fastapi import FastAPI,Path,HTTPException 
from fastapi.responses import JSONResponse
from schemas import Patient , PatientUpdate
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
    data[patient.id] = patient.model_dump(exclude=['id']) # converts from pydentic obj to dictonary
    
    # save the data into patient.json 
    saveData(data)

    return JSONResponse(
        status_code=201,
        content={"message": "Patient added Successfully !!",
                 "Patient_data":data[patient.id]}
    )



# PATCH :Update
@router.patch("/{id}")
def updatePatient(id:str, patient_update:PatientUpdate):
    try:
        data = loadData()
        if id not in data:
            raise HTTPException (status_code = 400 , detail = "Patient not found !")
        
        existing_patient_info=data[id]
        updated_patient_info =patient_update.model_dump(exclude_unset=True)
        for key , value in updated_patient_info.items():
            existing_patient_info[key] = value
        
        # to get the bmi or verdict
        # existing_patinet_info -> pydentic object ->update bmi or verdict 
        # -> pydantic obj -> dict 

        existing_patient_info["id"]=id
        patient_pydantic_obj = Patient(** existing_patient_info) #gives pydentic obj
        existing_patient_info=patient_pydantic_obj.model_dump(exclude=['id']) # this creates dict

        data[id]=existing_patient_info

        # saves data 
        saveData(data)
        return JSONResponse(status_code=200 , content = {"message":"data updated Sucessfully!",
                                                        "updated_data":data[id]})
    except Exception as e :
        raise HTTPException( status_code=500 , detail=f"{e}" )

    
#delete 
@router.delete("/{patient_id}")
def delete_patient(patient_id:str=Path(...,description='ID of Patient to be deleted',example='P001')):
    data = loadData()
    if  patient_id not in data:
        raise HTTPException(status_code=404 , detail="patient not found !")
    delete_patient = data.pop(patient_id)

    saveData(data)

    return JSONResponse(
        status_code= 200 , 
        content = {"message":f"Patient  is deleted Sucesssfully !",
                   "deleted_id":f"{patient_id}",
                   "deleted_data":delete_patient
                   }
    )

    
    