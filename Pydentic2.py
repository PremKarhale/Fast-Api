## Pydentic class is uded to check the text error or Data validation error 

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional

#Pydentic class
class Patient(BaseModel):
    #Fields
    name:str=Field(max_length=50)
    age:int=Field(gt=0 , lt=120)
    Email:EmailStr
    Linkdin_ID:AnyUrl
    weight:float=Field(gt=0)
    married:Optional[bool] = False # default set 
    allergies:Optional[List[str]]= None # default set 
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.Email)
    print(patient.contact_details['mob_no.']) # always access dictionary by [] and class using dot . !!


patient_info={'name':'prem','Email':'abc34@gmail.com','Linkdin_ID':'https://linkedin.com/322','age':23,'weight':60,'married':True,'contact_details':{"mob_no.":'234547484'}}
patient1=Patient(**patient_info)

insert_patient_data(patient1)