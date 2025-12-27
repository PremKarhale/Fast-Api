#model validator is used to apply the field constraints on more than two fields together 
# field validator hota he vo sirf single field he upar operate karta haii 
# or jo MOdel operator hota he vo pure pydentic fileds ke upar operate karta he 
from pydantic import BaseModel,EmailStr,AnyUrl,Field,model_validator
from typing import List,Dict,Optional,Annotated

#Pydentic class
class Patient(BaseModel):
    #Fields
    name:str
    age:int
    Email:EmailStr
    weight:float
    married:bool
    allergies:Optional[List[str]]= None # default set 
    contact_details:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contacts(cls,model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have emergency contact')
        else:
            return model


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.Email)
    print(patient.contact_details['mob_no.']) # always access dictionary by [] and class using dot . !!


patient_info={'name':'prem','Email':'abc34@gmail.com','age':65,'weight':60,'married':True,'contact_details':{"mob_no.":'234547484','emergency':'23456789'}}
patient1=Patient(**patient_info)

insert_patient_data(patient1)