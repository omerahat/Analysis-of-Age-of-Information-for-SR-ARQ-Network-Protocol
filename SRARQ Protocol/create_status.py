import numpy as np

def createStatus(probOfNACK=0.1):
    return np.random.rand() >= probOfNACK