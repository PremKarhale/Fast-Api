#Field validator is used to evaluate the field according to bussiness needs 
#field validator is a class method
#field validator is used to apply transformation on the filed


from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

#Pydentic class
class Patient(BaseModel):
    #Fields
    name:str
    age:int
    Email:EmailStr
    weight:float
    married:bool
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]

    @field_validator('Email')# takes field for valiadation , 
    @classmethod
    def email_validator(cls,value):
        valid_domin=['hdfc.com','sbi.com']
        #abc@gmail.com
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domin:
            raise ValueError('Not a valid Email')
        return value
    
    @field_validator('name')
    @classmethod
    def trasform_name(cls,value):
        return value.upper()


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.Email)
    print(patient.contact_details['mob_no.']) # always access dictionary by [] and class using dot . !!



patient_info={'name':'prem','Email':'abc34@hdfc.com','age':23,'weight':60,'married':True,'contact_details':{"mob_no.":'234547484'}}
patient1=Patient(**patient_info)

insert_patient_data(patient1)
