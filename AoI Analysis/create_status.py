import numpy as np

def createStatus(probOfNACK = 0.5):
    return np.random.rand() >= probOfNACK
 
