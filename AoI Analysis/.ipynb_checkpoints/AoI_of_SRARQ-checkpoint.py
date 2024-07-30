import random

def create_status(probOfNACK):
    return random.random() > probOfNACK

def AoI_of_SRARQ(windowSize=3, probOfNACK=0.1, packetCount=1000):
     packets = list(range(packetCount, 0, -1))
     window = [0] * windowSize
     step = 0
     aoi = {i: 0 for i in range(1, packetCount + 1)}  # Initialize AoI for each packet

     while packets or any(window):
          step += 1
          print(f"\n------ Step {step} ------")
          

                
    return aoi