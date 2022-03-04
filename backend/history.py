import json
# import tensorflow as tf
# from tensorflow import keras
# from sklearn.model_selection import train_test_split
# import numpy as np
from glob import glob
from PIL import Image
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
import os 
from io import BytesIO
import base64

def loss(history):
    plt.clf()
    plt.plot(history['loss'], 'b-', label='loss')
    if 'val_loss' in history:
        plt.plot(history['val_loss'], 'r--', label='val_loss')
    plt.xlabel('Epoch')
    plt.legend()
    img = BytesIO()
    plt.savefig(img, format='png', dpi=300)
    img.seek(0)
    return img

def accuracy(history):
    plt.clf()
    plt.plot(history['accuracy'], 'b-', label='accuracy')
    if 'val_accuracy' in history:
        plt.plot(history['val_accuracy'], 'r--', label='val_accuracy')
    plt.xlabel('Epoch')
    plt.legend()
    img = BytesIO()
    plt.savefig(img, format='png', dpi=300)
    img.seek(0)
    return img

# path = "react/mlweb/backend/deep_learning_models/TESTID_model_history.json"
# with open(path, 'r') as file:
#     history = file.read()
# history = json.loads(history)
# img = loss(history)
# print(img)