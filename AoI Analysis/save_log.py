import csv
import os

def saveLog(windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount, frequency, expected, logPath='log.csv'):
     # Check if the file already exists
     file_exists = os.path.isfile(logPath)

     with open(logPath, mode="a", newline='') as file:
          writer = csv.writer(file)

          # Write the header only if the file is being created for the first time
          if not file_exists:
               writer.writerow(["windowSize", "probOfBadChannel", "probOfBadNACK", "probOfGoodNACK", "packetCount", "expected", "frequency"])
          
          # Write the actual data
          writer.writerow([windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount, expected, frequency])