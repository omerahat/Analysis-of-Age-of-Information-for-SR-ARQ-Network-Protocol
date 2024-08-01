import pandas as pd

def calculatePi(filePath = "aoi_data.csv"):
     
     data = pd.read_csv(filePath)
     frequency = {}

     for index, row in data.iterrows():
          tupleAoI = tuple(row)
          if tupleAoI in frequency:
               frequency[tupleAoI] += 1
          else:
               frequency[tupleAoI] = 1
    
     return frequency
