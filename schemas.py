# Annotated : allows us to set the field
# Literal : it is used guide client to choose from required options only 

from pydantic import BaseModel , Field ,computed_field
from typing import Annotated ,Literal

class Patient(BaseModel):
    id:Annotated[str,Field(...,description='ID of the patient ',examples=['P001'])]
    name:Annotated[str,Field(...,description='Enter name of the patient',examples=['Suresh chavan'])]
    city:Annotated[str,Field(...,description='Enter name of city of Patient',examples=['Guwhati'])]
    age:Annotated[int,Field(...,description='Enter the age of the patient',examples=['34'])]
    gender:Annotated[Literal['male','female','other'],Field(...,description='Enter the gender of the patient',examples=['Male/Female'])]
    height:Annotated[float,Field(...,description='Enter the height of the patient in (m)',examples=['1.74 m'])]
    weight:Annotated[float,Field(...,description='Enter the weight of the patient in (kg)',examples=['60 kg'])]

@computed_field
@property
def bmi(self) -> float:
    bmi=self.weight/(self.height**2)  # bmi is a new field now 
    return bmi

@computed_field
@property
def verdict(self) -> str:
    if self.bmi < 18.5:
        return "UnderWeight"
    elif self.bmi < 30:
        return "Normal"
    else:
        return "Obese"