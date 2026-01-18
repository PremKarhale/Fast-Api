from fastapi import APIRouter,HTTPException
import pickle
import pandas as pd 
from schemas import userInput
from fastapi.responses import JSONResponse

#importing ml model / Creating Ml model
with open("model.pkl" , "rb") as f:
    model = pickle.load(f) 

router = APIRouter()

#Predict end point 
@router.post("/predict")
def predict_premimum(data: userInput):
    try:
        input_df=pd.DataFrame([{
        'income_lpa':data.income_lpa,  #input data in the dataframe
        'occupation':data.occupation,
        'age_group':data.age_group,
        'BMI':data.BMI,
        'lifeStyleRisk':data.lifeStyle_risk,
        'Tier_cities':data.city_tier
    }])
        prediction = model.predict(input_df)[0]
        prediction = prediction.item() 

        return JSONResponse(status_code=200 , content={"pridected_catagory":prediction})
    except Exception as e :
        raise HTTPException(status_code=500,detail=f"{e}")


  