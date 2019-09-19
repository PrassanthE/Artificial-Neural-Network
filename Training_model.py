# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:08:37 2019

@author: epras
"""

# Importing library
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('eptrain2.csv') #This CSV has all the collected training data
#dataset = pd.read_csv('prep.csv')
X = dataset.iloc[:, :-3].values #Storing all independent variables in X
y = dataset.iloc[:, 5:].values  #Storing all dependent variables in y

from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

#First hidden layer
classifier.add(Dense(10,input_shape = (5,), init = 'uniform', activation ='relu', ))

#Second Hidden layer
classifier.add(Dense(10,input_shape = (10,), init = 'uniform', activation ='relu'))

#Output layer
classifier.add(Dense(3,input_shape = (10,), init = 'uniform', activation ='softmax'))


classifier.compile(optimizer = 'adam', loss='binary_crossentropy', metrics= ['accuracy'])    
#Fitting
classifier.fit(X,y, batch_size = 16, nb_epoch = 100)

#Saving the model
classifier.save('epagent4ag')
