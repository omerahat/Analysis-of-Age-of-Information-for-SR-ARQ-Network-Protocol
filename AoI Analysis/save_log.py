import csv

def saveLog(windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount, frequency, expected,logPath='log.csv'):
     with open(logPath, mode="a", newline='') as file:
          writer = csv.writer(file)
          writer.writerow([windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount, expected, frequency])