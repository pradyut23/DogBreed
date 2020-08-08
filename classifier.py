from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np

def image_classification(img, weights_file):
    # Get all breeds from the txt files
    with open('breeds.txt', 'r') as reader:
        breeds=[]
        for breed in reader:
            try:
                breed=breed.replace('_',' ')
                breed=breed.title()
            except:
                breed=breed.title()
            breeds.append(breed[:-1])

    # Loading the model
    model = keras.models.load_model(weights_file)

    # Creating the array to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # Turning the image into a numpy array, normalizing and loading the image
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32)/255)
    data[0] = normalized_image_array

    # Prediction
    prediction = model.predict(data)
    return breeds[np.argmax(prediction)]
