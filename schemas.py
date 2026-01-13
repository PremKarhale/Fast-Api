# Annotated : allows us to set the field
# Literal : it is used guide client to choose from required options only 

from pydantic import BaseModel , Field ,computed_field
from typing import Annotated ,Literal , Optional

class Patient(BaseModel):
    id:Annotated[str,Field(...,description='ID of the patient ',examples=['P001'])]
    name:Annotated[str,Field(...,description='Enter name of the patient',examples=['Suresh chavan'])]
    city:Annotated[str,Field(...,description='Enter name of city of Patient',examples=['Guwhati'])]
    age:Annotated[int,Field(...,description='Enter the age of the patient',examples=['34'],gt=0 )]
    gender:Annotated[Literal['male','female','other'],Field(...,description='Enter the gender of the patient',examples=['Male/Female'])]
    height:Annotated[float,Field(...,description='Enter the height of the patient in (m)',examples=[1.74 ],gt=0)]
    weight:Annotated[float,Field(...,description='Enter the weight of the patient in (kg)',examples=[60 ],gt=0)]

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
        
class PatientUpdate(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None , gt=0)]
    gender:Annotated[Optional[str],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None ,gt=0)]
    weight:Annotated[Optional[float],Field(default=None , gt=0)]

    
