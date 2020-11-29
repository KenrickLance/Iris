from keras.models import load_model
import numpy as np

model = load_model('./learning/ct_scan.h5')

from skimage import io
from keras.preprocessing import image

img = image.load_img(r'C:\\Users\\Windows\\programming\\hack2020\\Iris\\project\\app\\learning\\ct_scans\\COVID\\Covid (1).png', grayscale=False, target_size=(64, 64))

disease_class=['Covid-19','Non Covid-19']

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x /= 255

prediction = model.predict(x)[0]
ind = np.argmax(prediction)
print('Prediction:',disease_class[ind])