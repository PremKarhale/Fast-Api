# THis is called as nested pydentic modelling 
#create two pydentic model and pass one as a field to ohter 

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

print(patient_obj)
print(patient_obj.name)
print(patient_obj.age)
print(patient_obj.address.pincode)