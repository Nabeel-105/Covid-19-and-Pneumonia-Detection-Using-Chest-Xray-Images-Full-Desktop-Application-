# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 00:47:40 2020

@author: nabeel
"""



import cv2
import numpy as np
from tensorflow.keras.models import  load_model
#from keras.optimizers import SGD

img_size=50
def covidtest(fln):
 
 filepath='D:/FYP with Updated DataSet/CovidPneumonia_Detection_savedmodel2'
 model=load_model(filepath,compile=True)

 print("model loaded :)")

 #testimagepath="D:/FYP with Updated DataSet/Split_Covid-Pneumonia_Dataset/test/Viral Pneumonia/Viral Pneumonia (750).png"
 #testimagepath="D:/FYP with Updated DataSet/Split_Covid-Pneumonia_Dataset/test/COVID-19/COVID-19(201).png"
 #testimagepath="D:/FYP with Updated DataSet/Split_Covid-Pneumonia_Dataset/test/NORMAL/Normal (2157).jpg"
 img = cv2.imread(fln)
 img = cv2.resize(img,(img_size,img_size))
 img = np.reshape(img,[-1,img_size,img_size,3])
 img = np.array(img)
 classes = model.predict_classes(img , axis=1)
 if classes==0:
     print("covid")
 elif classes==1:
     print("Normal")
 elif classes==2:
     print("Pneumonia")
 return(classes)
 
 

