# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:17:22 2020

@author: nabeel
"""



import splitfolders
path = "D:/FYP with Updated DataSet/NewDataSet"


splitfolders.ratio(path, output="Split_Covid-Pneumonia_Dataset", seed=1337,ratio=(.7, .1,.2))