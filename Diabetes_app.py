from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

origins=['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# Loading the save ModelInput
diabetes_model = pickle.load(open('trained_model.sav', 'rb'))

@app.post('/diabetes_prediction')

def diabetes_prediction(input_parameters: ModelInput):
    input_data = input_parameters.json()
    input_dict = json.loads(input_data)

    preg=input_dict['Pregnancies']
    glu=input_dict['Glucose']
    bp=input_dict['BloodPressure']
    st=input_dict['SkinThickness']
    ins=input_dict['Insulin']
    bmi=input_dict['BMI']
    dpf=input_dict['DiabetesPedigreeFunction']
    age=input_dict['Age']

    input_list = [preg, glu, bp, st, ins, bmi, dpf, age]

    prediction= diabetes_model.predict([input_list])
    # Return the prediction result
    # 0 for not diabetic, 1 for diabetic
    if prediction[0]==0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
