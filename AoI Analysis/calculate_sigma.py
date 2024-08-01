import pandas as pd
from calculate_AoI import calculateAoI

def calculateSigma(filePath = "aoi_data.csv"):
    data = pd.read_csv(filePath)
    AoIDict = {}

    for index, row in data.iterrows():
        row_tuple = tuple(row)  # Convert the row to a tuple to use as a dictionary key
        row_list = row.tolist()  # Convert the row to a list
        if row_tuple not in AoIDict:
            AoIDict[row_tuple] = calculateAoI(3, window=row_list)  # Pass the list
        else:
            pass

    return AoIDict
