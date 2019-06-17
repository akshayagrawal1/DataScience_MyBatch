# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:02:18 2017

@author: Srikanth Dakoju
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset_train = pd.read_csv('Google_Stock_Price_Train.csv')

training_set = dataset_train.iloc[:,1:2].values

#plt.plot(training_set)

# Data Preprocessing

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))
training_set_scaled = sc.fit_transform(training_set)

X_train = []
y_train = []

for i in range(60,1258):
    X_train.append(training_set_scaled[i-60:i,0])
    y_train.append(training_set_scaled[i,0])
    
X_train = np.array(X_train) 
y_train = np.array(y_train)




# Creating RNN (Recurrent Neural Network)
# Importing required libraries

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout


srikanth = Sequential()
# ctrl + i  --> for help 
srikanth.add(LSTM(units = 50,
                   return_sequences = True, 
                   input_shape = (X_train.shape[1],1)))
srikanth.add(Dropout(0.2))
srikanth.add(LSTM(units = 50,
                   return_sequences = True))
srikanth.add(Dropout(0.2))
srikanth.add(LSTM(units = 50,
                   return_sequences = True))
srikanth.add(Dropout(0.2))
srikanth.add(LSTM(units = 50))
srikanth.add(Dropout(0.2))

# Adding the output layer
srikanth.add(Dense(units = 1))


# compileing and training
srikanth.compile(optimizer= 'adam',
                  loss = 'mean_squared_error')

srikanth.fit(X_train,y_train, epochs = 100,
              batch_size = 32)



# Data Preprocessing 

dataset_test = pd.read_csv('Google_Stock_Price_Test.csv')


real_stock_price = dataset_test.iloc[:,1:2].values


# combine the dataset 

dataset_total = pd.concat((dataset_train['Open'],
                           dataset_test['Open']), axis = 0)


inputs = dataset_total[len(dataset_total)- 
                       len(dataset_test) -60:].values

inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

X_test = []

for i in range(60,80):
    X_test.append(inputs[i-60:i,0])

X_test = np.array(X_test)
X_test = np.reshape(X_test,(X_test.shape[0],
                            X_test.shape[1],1))

##

predicted_stock_price = srikanth.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)


# Visulation

plt.plot(real_stock_price,color ='red',
         label = 'Real Google price')

plt.plot(predicted_stock_price,color ='blue',
         label = 'Predict Google price')




