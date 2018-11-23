#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

def create_model(optimizer='adam'):
    #create sequential
    model = Sequential()
    model.add(Dense(12,input_dim = 8,activation='relu'))
    model.add(Dense(1,activation='sigmoid'))
    #compile model
    model.compile(loss='binary_crossentropy',optimizer=optimizer,metrics=['accuracy'])
    return model

seed = 7
np.random.seed(seed)
#load dataset
dataset = np.loadtxt('pima-indians-diabetes.csv',delimiter=',')
#split into ,nput and output variables
X = dataset[:,0:8]
Y = dataset[:,8]
#create 
model = KerasClassifier(build_fn=create_model,epochs=100,batch_size=10,verbose=0)
optimizer = ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']
param_grid = dict(optimizer=optimizer)
grid = GridSearchCV(estimator=model,param_grid=param_grid,n_jobs=1)
grid_result = grid.fit(X,Y)
# summarize results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
    