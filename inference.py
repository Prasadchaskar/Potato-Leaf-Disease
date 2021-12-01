import numpy as np
from numpy.lib.type_check import imag
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array,array_to_img
from tensorflow.python import keras

classes = ['Potato___Early_blight','Potato___Late_blight','Potato___healthy']
model = keras.models.load_model('potato.h5')

def predict(img_path):
    image = load_img(img_path,target_size=(256,256))
    image = img_to_array(image)
    image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    yhat = np.array(yhat)
    indices = np.argmax(yhat,axis=1)
    predicted = [classes[i] for i in indices]
    output = predicted[0]
    return output
