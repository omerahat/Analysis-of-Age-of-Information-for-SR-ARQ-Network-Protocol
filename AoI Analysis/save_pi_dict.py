import csv

def savePiDict(data, file_path='frequency_data.csv'):
     with open(file_path, mode='w', newline='') as file:
          writer = csv.writer(file)
          writer.writerow(["Tuple", "AoI"])
          for key, value in data.items():
               writer.writerow([key, value])
