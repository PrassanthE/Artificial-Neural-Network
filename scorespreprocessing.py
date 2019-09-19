# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:36:00 2019

@author: epras
"""
import pandas as pd

dataset = pd.read_csv('scores.csv')
a =  dataset.iloc[:, :].values
b = []
if a[:,[5]] == 1:
    b.append(a.all())