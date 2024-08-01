import pandas as pd

def calculateExpected(freqFilePath = "frequency_data.csv", AoIDictFilePath = "aoi_dict.csv"):
     frequencyData = pd.read_csv(freqFilePath)
     AoIDict = pd.read_csv(AoIDictFilePath)
     
     merged_data = pd.merge(frequencyData, AoIDict, on='Tuple', suffixes=('_freq', '_dict'))

     # Multiply the corresponding AoI values
     merged_data['AoI_product'] = merged_data['AoI_freq'] * merged_data['AoI_dict']

     # Calculate the length of aoi_data
     length_of_data = frequencyData["AoI"].sum()

     # Calculate the sum of AoI products
     sum_aoi_product = merged_data['AoI_product'].sum()

     # Divide the sum by the length of aoi_data.csv
     result = sum_aoi_product / length_of_data

     return result

# Test the function
print(calculateExpected())