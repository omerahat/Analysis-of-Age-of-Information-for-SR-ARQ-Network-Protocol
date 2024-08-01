import csv

def savePiDict(data, file_path='aoi_dict.csv'):
     with open(file_path, mode='w', newline='') as file:
          writer = csv.writer(file)
          writer.writerow(["Tuple", "AoI"])
          for key, value in data.items():
               writer.writerow([key, value])
