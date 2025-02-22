import numpy 
from Normalize import normalize

def vectorization(img): 
    vector = numpy.zeros(784)
    img = normalize(img)
    vector = img.flatten()
    return vector

def get(data):
    arrayVector = numpy.zeros((data.shape[0], data[0].shape[0] * data[1].shape[1]))
    for i in range(data.shape[0]):
        arrayVector[i] = vectorization(data[i])
    return arrayVector
