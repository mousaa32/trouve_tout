import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

DATADIR="/home/moussa/Documents/PROJET/projethtml/trouve_tout"
CATEGORIES=["compare","images"]
IMG_SIZE=30
# new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
# plt.imshow(img_array,cmap="gray")
# plt.show()
training_data=[]
def create_training_data():
    for categorie in CATEGORIES:
        path=os.path.join(DATADIR,categorie)
        class_num=CATEGORIES.index(categorie)
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass

create_training_data()  
# print(len(training_data))      
random.shuffle(training_data)
# for sample in training_data[:3]:
#     print(sample[1])
x=[]
y=[]
for features,label in training_data:
    x.append(features)
    y.append(label)
x=np.array(x).reshape(-1,IMG_SIZE,IMG_SIZE,1)
print(x)