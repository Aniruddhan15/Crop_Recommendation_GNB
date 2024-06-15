# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:21:03 2024

@author: aniru
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open("C:/ML_API/Python_Code/finalized_model.sav", 'rb'))


# creating a function for Prediction

def Crop_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0] == 20:
        print('Rice')
    elif prediction[0] == 11:
        print('Maize')
    elif prediction[0] == 3:
        print('ChickPea')
    elif prediction[0] == 9:
        print('KidneyBeans')
    elif prediction[0] == 18:
        print('PigeonPeas')
    elif prediction[0] == 13:
        print('MothBeans')
    elif prediction[0] == 14:
        print('MungBean')
    elif prediction[0] == 2:
        print('Blackgram')
    elif prediction[0] == 10:
        print('Lentil')
    elif prediction[0] == 19:
        print('Pomegranate')
    elif prediction[0] == 1:
        print('Banana')
    elif prediction[0] == 12:
        print('Mango')
    elif prediction[0] == 7:
        print('Grapes')
    elif prediction[0] == 21:
        print('Watermelon')
    elif prediction[0] == 15:
        print('Muskmelon')
    elif prediction[0] == 0:
        print('Apple')
    elif prediction[0] == 16:
        print('Orange')
    elif prediction[0] == 17:
        print('Papaya')
    elif prediction[0] == 4:
        print('Coconut')
    elif prediction[0] == 6:
        print('Cotton')
    elif prediction[0] == 8:
        print('Jute')
    elif prediction[0] == 5:
        print('Coffee')
    else:
        print('Unknown Crop')
    
  
def main():
    
    
    # giving a title
    st.title('Crop Prediction Web App')
    
    
    # getting the input data from the user
    #'Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity',
    #       'pH_Value', 'Rainfall'
    
    Nitrogen = st.text_input('Nitrogen reqd')
    Phosphorus = st.text_input('phosphorus reqd')
    Potassium = st.text_input('potassium reqd')
    Temperature = st.text_input('temperature reqd')
    Humidity = st.text_input('humidity reqd')
    pH_Value = st.text_input('ph value reqd')
    Rainfall = st.text_input('rainfall reqd')
 
    
    
    # code for Prediction
    Pred = ''
    
    # creating a button for Prediction
    
    if st.button('Crop to be used '):
        Pred = Crop_prediction([Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH_Value, Rainfall])
        
        
    st.success(Pred)
    
    
    
    
    
if __name__ == '__main__':
    main()