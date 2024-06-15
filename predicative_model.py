# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:11:31 2024

@author: aniru
"""

import numpy as np
import pickle

loaded_model = pickle.load(open("C:/ML_API/Python_Code/finalized_model.sav",'rb'))

input_data = (85,58,41,21.7,80.3,7.03,226.6)
input_data_as_numpy_array = np.asarray(input_data)
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

