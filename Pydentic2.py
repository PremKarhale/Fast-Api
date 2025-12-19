from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    age:int
    weight:float 
    married:Optional[bool] = False # default set 
    allergies:Optional[List[str]]= False # default set 
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details['email']) # always access dictionary by [] and class using dot . !!


patient_info={'name':'prem','age':23,'weight':60,'married':True,'contact_details':{'email':'prem@1234','mob_no.':'234547484'}}
patient1=Patient(**patient_info)

insert_patient_data(patient1)