#computed filed is used to draw some extra field using existing fields 

from pydantic import BaseModel,EmailStr,AnyUrl,Field,computed_field
from typing import List,Dict,Optional,Annotated

#Pydentic class
class Patient(BaseModel):
    #Fields
    name:str
    age:int
    Email:EmailStr
    Linkdin_ID:AnyUrl
    weight:float #kg
    height:float #mtr
    married:bool=False
    allergies:Optional[List[str]]= None # default set 
    contact_details:Dict[str,str]

    @computed_field
    @property              ## computed filed bmi is ready  
    def bmi(self)->float: # it takes instance of pydentic model as input ->that gives ans in float
        bmi = round(self.weight/(self.height)**2,2)
        return bmi

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(f'Bmi of the patient name {patient.name} is:',patient.bmi)
    print(patient.contact_details['mob_no.']) # always access dictionary by [] and class using dot . !!


patient_info={'name':'prem','Email':'abc34@gmail.com','Linkdin_ID':'https://linkedin.com/322','age':23,'weight':60,'height':1.72,'married':True,'contact_details':{"mob_no.":'234547484'}}
patient1=Patient(**patient_info)

insert_patient_data(patient1)