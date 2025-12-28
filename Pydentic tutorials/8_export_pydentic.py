# Pydentic model gives us varity of choices to export the model as json or in dict
from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str              #pydentic modl passed as a field to class Patient 
    pincode:str

class Patient(BaseModel):
    name:str
    age:int
    address:Address

address ={'city':'sambhaji nagar','state':'Mah','pincode':'12345'}
patient_dtl ={'name':'prem','age':21,'address':address}

Address1 = Address(**address)
patient_obj = Patient(**patient_dtl)

temp=patient_obj.model_dump()  # Export patient data as dict 
print(temp)

temp1 = patient_obj.model_dump_json(include={'name':True,'address':'city'})# Export patient data as json
print(temp1) 
print(type(temp1))#json

# include , exclude or exclude_unset=True are the inputs used in model_dump 
#exclude_unset=True is used to exclude the fields that are not set at the time of obj creation 