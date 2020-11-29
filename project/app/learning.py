from keras.models import load_model
import numpy as np

from skimage import io
from keras.preprocessing import image

from django.conf import settings

model = load_model(f'{settings.BASE_DIR}/app/learning/ct_scan.h5')

def ct_scan_analyze(path):
	img = image.load_img(path, grayscale=False, target_size=(64, 64))

	disease_class=['Covid-19 Positive','Covid-19 Negative']

	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x /= 255

	prediction = model.predict(x)[0]
	ind = np.argmax(prediction)
	return f'Prediction: {disease_class[ind]}'