from numpy.lib.stride_tricks import as_strided
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
from glob import glob
from PIL import Image
import matplotlib.pyplot as plt
import os
import base64
from io import BytesIO
import json

# print(tf.__version__)
# print(keras.__version__)

imgObjs = glob('./datas/*/*.png')
labels = ["apple", "beef", "milk","noodle","potato"]
dic = {"apple":0, "beef":1, "milk":2, "noodle":3, "potato":4}

# def plot_image(i, predictions_array, true_label, img):
#     predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
#     plt.grid(False)
#     plt.xticks([])
#     plt.yticks([])

#     plt.imshow(img)

#     predicted_label = np.argmax(predictions_array)
#     if predicted_label == true_label:
#         color = 'blue'
#     else:
#         color = 'red'

#     plt.xlabel("{} {:2.0f}% ({})".format(class_name[predicted_label],
#                                 100*np.max(predictions_array),
#                                 class_name[true_label]),
#                                 color=color)

# def plot_value_array(i, predictions_array, true_label):
#     predictions_array, true_label = predictions_array[i], true_label[i]
#     plt.grid(False)
#     #plt.xticks([])
#     plt.xticks(range(N_CLASS), class_name, rotation=90)
#     plt.yticks([])
#     thisplot = plt.bar(range(N_CLASS), predictions_array, color="#777777")
#     plt.ylim([0, 1]) 
#     predicted_label = np.argmax(predictions_array)
 
#     thisplot[predicted_label].set_color('red')
#     thisplot[true_label].set_color('blue')

# db에서 이미지 데이터, 이름을 따로 불러옴

class DeepLearningHelper():
    def __init__(self, datas):
        images= []
        names = []
        for data in datas:
            img = base64.decodestring( data['imageData'] )
            images.append( BytesIO(img) )
            name = data['name'].split("_")[0]
            names.append( name )
        
        self.class_dic = dict()
        self.X = self.__xpreprocessing__(images)
        self.Y = self.__ypreprocessing__(names)
        # self.set_hyper_parameters_option()
        # self.preprocessing()

    def __xpreprocessing__(self, datas):
        xlist = []
        for data in datas:
            image = Image.open(data)
            image = image.resize((128, 128))
            image = np.array(image)
            xlist.append(image)  
        #리스트를 np_array에 담고, 픽셀 값을 0~1사이로 조정
        # return (np.array(xlist).astype(np.float32) / 255.) 
        return np.array(xlist)

    def __ypreprocessing__(self, names):
        name_set = set(names)
        for idx, name in enumerate(name_set):
            self.class_dic[name] = idx

        ylist = []
        for name in names:
            label = self.class_dic[name] 
            ylist.append(label)

        # 리스트를 np_array에 담고, label을 onehot-encoding
        # return keras.utils.to_categorical( np.array(ylist) ) 
        return np.array(ylist)

    def preprocessing(self): # 2순위
        self.train_images, self.test_images, self.train_labels, self.test_labels = train_test_split(self.X, self.Y, test_size=0.2, 
                                                    shuffle=True, random_state=44)

        self.train_labels = self.train_labels[..., tf.newaxis]
        self.test_labels = self.test_labels[..., tf.newaxis]
        
        self.N_TRAIN = self.train_images.shape[0]
        self.N_TEST = self.test_images.shape[0]

        self.train_images = self.train_images.astype(np.float32) / 255.
        self.test_images = self.test_images.astype(np.float32) / 255.

        self.train_labels = keras.utils.to_categorical(self.train_labels)
        self.test_labels = keras.utils.to_categorical(self.test_labels)

        self.train_dataset = tf.data.Dataset.from_tensor_slices((self.train_images, self.train_labels)).shuffle(
                buffer_size=2372).batch(self.N_BATCH).repeat()
        self.test_dataset = tf.data.Dataset.from_tensor_slices((self.test_images, self.test_labels)).batch(
				self.N_BATCH)

        self.steps_per_epoch = self.N_TRAIN//self.N_BATCH
        self.validation_steps = self.N_TEST//self.N_BATCH

    def set_hyper_parameters_option(self, batch, learning_rate=0.01 , epoch=10):  # 1순위
        self.learning_rate = learning_rate
        self.N_EPOCHS = epoch
        self.N_BATCH = batch
        self.N_CLASS = len(self.class_dic)

    def create_model(self):        # 3순위
        self.model = keras.Sequential()
        self.model.add(keras.layers.Conv2D(filters=32, kernel_size=3, 
                                    activation='relu', padding='SAME', 
                                    input_shape=(128, 128, 3)))
        self.model.add(keras.layers.MaxPool2D(padding='SAME'))
        self.model.add(keras.layers.Conv2D(filters=64, kernel_size=3, 
                                    activation='relu', padding='SAME'))
        self.model.add(keras.layers.MaxPool2D(padding='SAME'))
        self.model.add(keras.layers.Conv2D(filters=128, kernel_size=3, 
                                    activation='relu', padding='SAME'))
        self.model.add(keras.layers.MaxPool2D(padding='SAME'))
        self.model.add(keras.layers.Flatten())
        self.model.add(keras.layers.Dense(256, activation='relu'))
        self.model.add(keras.layers.Dropout(0.4))
        self.model.add(keras.layers.Dense(3, activation='softmax'))

        self.model.compile(optimizer=tf.keras.optimizers.Adam(self.learning_rate),
                loss='categorical_crossentropy',
                metrics=['accuracy'])
        # self.model.summary()
    
    def training(self): #4순위
        self.history = self.model.fit(self.train_dataset, epochs=self.N_EPOCHS, steps_per_epoch=self.steps_per_epoch, 
                    validation_data=self.test_dataset, validation_steps=self.validation_steps)

    def save(self, id): # 마지막
        modelpath = f"react/mlweb/backend/deep_learning_models/{id}_model.h5"

        # modelpath = "model.h5"
        self.model.save(modelpath)
        historypath = f"react/mlweb/backend/deep_learning_models/{id}_model_history.json"
        # historypath = "model_history.json"
        with open(historypath, 'w') as file:
            json.dump(self.history.history, file)    
        
    def __del__(self):
        print("deep_class del")