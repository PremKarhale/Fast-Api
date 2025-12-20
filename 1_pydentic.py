
# Basic working of Pydentic 
# pydentic is used for text validation or data validation 

from pydantic import BaseModel

class Patient(BaseModel):     ##Pydentic class 
    name:str
    age:int

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)

patient_info={'name':'nitish','age':'30'}
patient1=Patient(**patient_info)    

insert_patient_data(patient1)