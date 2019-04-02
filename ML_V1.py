from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
def create_model_cnn():
  model=Sequential()

  model.add(Conv2D(128, (3, 3), input_shape = (300, 300, 3), activation = 'relu'))
  model.add(MaxPooling2D(pool_size = (3, 3)))

  model.add(Conv2D(128, (3, 3), activation = 'relu'))
  model.add(MaxPooling2D(pool_size = (3, 3)))

  model.add(Conv2D(128, (3, 3), activation = 'relu'))
  model.add(MaxPooling2D(pool_size = (3, 3)))

  model.add(Flatten())        
  model.add(Dense(600, activation='relu'))
  model.add(Dense(200, activation='sigmoid'))
  model.add(Dense(9, activation='softmax'))

  model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
  
  return model

load_model =create_model_cnn()

load_model.load_weights('./test.h5')

import os
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras import optimizers
import cv2                                                                  #import opencv lib. 
import numpy as np
from keras.preprocessing import image
folderT = ['./test']
preimg = []  
T = ['coat','jeans','polo shirts','shirts','shot pants','shot shirts','sport shirts','T-Shirts','trousers']                
def load_images_from_folder(folder):                      
    for filename in os.listdir(folder):                           
          img = cv2.imread(os.path.join(folder, filename))          
          img = cv2.resize(img, (300, 300))
          img =image.img_to_array(img)                                  
          preimg.append(img)                                                  
          
          
for folder in folderT:                                                            
  print('Reading images from path: ' + folder)
  load_images_from_folder(folder)   

del folderT

preimg=np.array(preimg)/255
print(preimg.shape)

#y_prob = final_model_cnn.predict(preimg) 
y_prob = load_model.predict(preimg) 
y_classes = y_prob.argmax(axis=-1)
ans=y_classes[0]

ans=[]

for i in range(len(preimg)):
  ans.append(T[y_classes[i]])
print(ans)