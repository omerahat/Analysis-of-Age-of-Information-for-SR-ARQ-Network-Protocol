import csv

def saveAoIArray(data, filename='aoi_data.csv'):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    