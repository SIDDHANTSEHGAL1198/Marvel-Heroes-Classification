# -*- coding: utf-8 -*-
"""Marvel_Avengers_assemble.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1weHv10QRvrmP_7Dzl60y-EwUxKVX7QMc
"""

!pip install kaggle

!mkdir /root/.kaggle/

!cp /content/drive/MyDrive/Key/kaggle.json /root/.kaggle/

!kaggle datasets download -d hchen13/marvel-heroes

!unzip -d /content/Avengers_Assemble/ /content/marvel-heroes.zip

"""# Importing libraries"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import plotly.express as px
import seaborn as sns
from keras.preprocessing.image import ImageDataGenerator

from keras.models import Input,Model
from keras.layers import Dense,Activation,Dropout,Flatten,MaxPool2D,Conv2D
from keras.applications.inception_v3 import InceptionV3,preprocess_input,decode_predictions

"""# Preprocessing Training set"""

train_datagen=ImageDataGenerator(rescale=1./255,horizontal_flip=True,rotation_range=20,
                                 height_shift_range=0.1,width_shift_range=0.1,
                                 shear_range=0.2,zoom_range=0.2)

training_set=train_datagen.flow_from_directory('/content/Avengers_Assemble/marvel/train',target_size=(256,256),class_mode='categorical',
                                               batch_size=32,shuffle=True)

"""# Preprocessing Test set

"""

test_datagen=ImageDataGenerator(rescale=1./255)

test_set=test_datagen.flow_from_directory('/content/Avengers_Assemble/marvel/valid',
                                          target_size=(256,256),class_mode='categorical',
                                          batch_size=32,shuffle=True)

"""# Dataset Inspection"""

from keras.preprocessing import image
import matplotlib.image as img

"""**And I am IRON MAN**"""

path1='/content/Avengers_Assemble/marvel/train/ironman/pic_390.jpg'
plt.imshow(img.imread(path1))

"""**Hulk Smash**"""

path2='/content/Avengers_Assemble/marvel/train/hulk/pic_002.jpg'
plt.imshow(img.imread(path2))

"""**I can do this all day**"""

path3='/content/Avengers_Assemble/marvel/train/captain america/pic_004.jpg'
plt.imshow(img.imread(path3))

"""**Dormammu, I've Come To Bargain**"""

path4='/content/Avengers_Assemble/marvel/train/doctor strange/pic_008.jpg'
plt.imshow(img.imread(path4))

"""**YOU COULD NOT LIVE WITH YOUR OWN FAILURE, AND WHERE DID THAT BRING YOU?**"""

path5='/content/Avengers_Assemble/marvel/train/thanos/pic_005.jpg'
plt.imshow(img.imread(path5))

"""# Making CNN Architecture"""

ptm=InceptionV3(input_shape=(256,256,3),weights='imagenet',include_top=False)
for layer in ptm.layers:
    layer.trainable = False

flat=Flatten()(ptm.output)
out=Dense(units=8,activation='softmax')(flat)
model=Model(inputs=ptm.input,outputs=out)

from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
checkpoint = ModelCheckpoint('InceptionV3_model.h5', verbose=1, save_best_only=True)

"""# Compiling the Model"""

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

model.summary()

"""# Flow-Chart"""

tf.keras.utils.plot_model(model=model,to_file='inception_archi.png',show_shapes=True)

"""# Training Model"""

model.fit(x=training_set,validation_data=test_set,epochs=40,callbacks=checkpoint)

from keras.models import load_model
model.save("avengers_network.h5")

model_saved=load_model('/content/avengers_network.h5')

metrics=pd.DataFrame(model.history.history)

metrics

metrics[['loss','val_loss']].plot()

metrics[['accuracy','val_accuracy']].plot()

dct=training_set.class_indices
dct

lst=[]
for x in dct.keys():
  lst.append(x)
lst

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

"""# Results

**Test Case-1**
"""

img_path='/content/drive/MyDrive/Test Cases/images.jpg'
img = image.load_img(img_path, target_size=(256,256))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


result=model_saved.predict(x)
res=lst[np.argmax(result)]

print("Model Prediction=>",res)
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)

"""**Test Case-2**"""

img_path='/content/drive/MyDrive/Test Cases/iron_mam.jpg'
img = image.load_img(img_path, target_size=(256,256))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


result=model_saved.predict(x)
res=lst[np.argmax(result)]

print("Model Prediction=>",res)
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)

"""**Test-Case-3**"""

img_path='/content/drive/MyDrive/Test Cases/KwSeU4dvFnJkPJ9FWXNSk3.jpg'
img = image.load_img(img_path, target_size=(256,256))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


result=model_saved.predict(x)
res=lst[np.argmax(result)]

print("Model Prediction=>",res)
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)

"""**Test Case-4**"""

img_path='/content/drive/MyDrive/Test Cases/9c4719c85686690107d73bae04c0889d5cb44d55.jpg'
img = image.load_img(img_path, target_size=(256,256))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


result=model_saved.predict(x)
res=lst[np.argmax(result)]

print("Model Prediction=>",res)
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)

"""**Test Case-5**"""

img_path='/content/drive/MyDrive/Test Cases/010fe43b47f41f3bc992014ab93f01996772f099.jpg'
img = image.load_img(img_path, target_size=(256,256))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


result=model_saved.predict(x)
res=lst[np.argmax(result)]

print("Model Prediction=>",res)
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)

"""**Test-Case-6**"""

img_path='/content/drive/MyDrive/Test Cases/loki-1556801363.jpeg'
img = image.load_img(img_path, target_size=(256,256))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


result=model_saved.predict(x)
res=lst[np.argmax(result)]

print("Model Prediction=>",res)
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)

"""**Test Case-7**"""

img_path='/content/drive/MyDrive/Test Cases/SQEX_Blog_Cap_Image2-2p6omydfp.jpg'
img = image.load_img(img_path, target_size=(256,256))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


result=model_saved.predict(x)
res=lst[np.argmax(result)]

print("Model Prediction=>",res)
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)

