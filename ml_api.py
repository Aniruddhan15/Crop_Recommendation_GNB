# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:30:09 2024

@author: aniru
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()
class model_input(BaseModel):
    
    Nitrogen : int
    Phosphorus : int
    Potassium : int
    Temperature : float
    Humidity : float
    pH_Value : float
    Rainfall : float
        
# loading the saved model
Crop_model = pickle.load(open('finalized_model.sav', 'rb'))

@app.post('/Crop_prediction')
def Crop_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    nitro = input_dictionary['Nitrogen']
    phos = input_dictionary['Phosphorus']
    pot = input_dictionary['Potassium']
    temp = input_dictionary['Temperature']
    hum = input_dictionary['Humidity']
    ph = input_dictionary['pH_Value']
    rain = input_dictionary['Rainfall']
    
    
    input_list = [nitro,phos,pot,temp,hum,ph,rain]
    
    prediction = Crop_model.predict([input_list])
    
    if prediction[0] == 20:
        return 'Rice'
    elif prediction[0] == 11:
        return 'Maize'
    elif prediction[0] == 3:
        return 'ChickPea'
    elif prediction[0] == 9:
        return 'KidneyBeans'
    elif prediction[0] == 18:
        return 'PigeonPeas'
    elif prediction[0] == 13:
        return 'MothBeans'
    elif prediction[0] == 14:
        return 'MungBean'
    elif prediction[0] == 2:
        return 'Blackgram'
    elif prediction[0] == 10:
        return 'Lentil'
    elif prediction[0] == 19:
        return 'Pomegranate'
    elif prediction[0] == 1:
        return 'Banana'
    elif prediction[0] == 12:
        return 'Mango'
    elif prediction[0] == 7:
        return 'Grapes'
    elif prediction[0] == 21:
        return 'Watermelon'
    elif prediction[0] == 15:
        return 'Muskmelon'
    elif prediction[0] == 0:
        return 'Apple'
    elif prediction[0] == 16:
        return 'Orange'
    elif prediction[0] == 17:
        return 'Papaya'
    elif prediction[0] == 4:
        return 'Coconut'
    elif prediction[0] == 6:
        return 'Cotton'
    elif prediction[0] == 8:
        return 'Jute'
    elif prediction[0] == 5:
        return 'Coffee'
    else:
        return 'Unknown Crop'

