# Annotated : allows us to set the field
# Literal : it is used guide client to choose from required options only 
# @computed filed : when i have to create multiple fields from exitsting fields 

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



# Models Pydantic Class **

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]


## pydantic model to validate the input fields 
class userInput(BaseModel):
    age:Annotated[int,Field(...,gt=0 , lt=120 ,description="Age of the user")]
    weight:Annotated[float,Field(...,gt=0,description="weight of the user")]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description="height of the user")]
    income_lpa:Annotated[float,Field(...,gt=0,description="Income of the user")]
    smoker:Annotated[bool,Field(...,description="Is user a smoker")]
    city:Annotated[str,Field(...,description="City that user belongs to ")]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'],Field(...,description="Occupation of the User")]

    
    @computed_field
    @property
    def BMI(self)->float:
        bmi =self.weight/(self.height)**2
        return bmi
     
    @computed_field
    @property
    def lifeStyle_risk(self)->str:
        if self.smoker and self.BMI > 30:
            return "high"
        elif self.smoker and self.BMI < 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self)->str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
    





