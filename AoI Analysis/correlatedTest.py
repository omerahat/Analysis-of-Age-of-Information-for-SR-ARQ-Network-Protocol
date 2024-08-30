from AoI_of_SRARQ import AoIOfSRARQ
from calculate_AoI import calculateAoI
from save_AoI_array import saveAoIArray
from save_AoI_file import saveAoIFile
from calculate_pi import calculatePi
from save_pi_dict import savePiDict
from calculate_sigma import calculateSigma
from save_sigma_dict import savePiDict  # Corrected: savePiDict to saveSigmaDict
from calculate_expected import calculateExpected
from save_log import saveLog
import time
import os

repeat = 7
windowSizes = [2,3,4,5,6,7,8,9]
probOfBadChannels = [0.01,0.02,0.05,0.1,0.2]
probOfBadNACKs = [0.7,0.8,0.9] 
probOfGoodNACKs = [0.01,0.05,0.1] 
packetCounts = [100,1000,10000,100000,1000000]

# Create a folder using an absolute path
curr_time = time.strftime("%d_%m_%Y_%H.%M.%S")  # Avoid colons in folder name
folder_name = os.path.abspath(curr_time)
os.makedirs(folder_name, exist_ok=True)  # Safely create directory if it doesn't exist

# Create parameters file in the newly created folder
parameters_file_path = os.path.join(folder_name, "parameters.txt")
with open(parameters_file_path, "w") as f:
     f.write(f"repeat: {repeat}\n")
     f.write(f"windowSize: {windowSizes}\n")
     f.write(f"probOfBadChannel: {probOfBadChannels}\n")
     f.write(f"probOfBadNACK: {probOfBadNACKs}\n")
     f.write(f"probOfGoodNACK: {probOfGoodNACKs}\n")
     f.write(f"packetCount: {packetCounts}\n")

def run(windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount):
     """
     Run the SR ARQ simulation and save results for given parameters.

     :param windowSize: Size of the window.
     :param probOfBadChannel: Probability of a bad channel.
     :param probOfBadNACK: Probability of a bad NACK.
     :param probOfGoodNACK: Probability of a good NACK.
     :param packetCount: Number of packets in the simulation.
     """
     data = AoIOfSRARQ(windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount)
     
     # Use absolute paths for saving files
     aoi_data_filename = os.path.join(folder_name, f"aoi_data_{windowSize}_{probOfBadChannel}_{probOfBadNACK}_{probOfGoodNACK}_{packetCount}.csv")
     saveAoIArray(data, aoi_data_filename)
     
     AoI = []
     for window in data:
          AoI.append(calculateAoI(windowSize, window))

     aoi_filename = os.path.join(folder_name, f"AoI_{windowSize}_{probOfBadChannel}_{probOfBadNACK}_{probOfGoodNACK}_{packetCount}.csv")
     saveAoIFile(AoI, aoi_filename)

     # Save frequency and sigma data to files
     frequency_filename = os.path.join(folder_name, f"frequency_data_{windowSize}_{probOfBadChannel}_{probOfBadNACK}_{probOfGoodNACK}_{packetCount}.csv")
     sigma_filename = os.path.join(folder_name, f"sigma_data_{windowSize}_{probOfBadChannel}_{probOfBadNACK}_{probOfGoodNACK}_{packetCount}.csv")
     frequency = calculatePi(aoi_data_filename)
     savePiDict(frequency, frequency_filename)

     AoIdict = calculateSigma(aoi_data_filename)
     savePiDict(AoIdict, sigma_filename)

     # Pass file paths instead of dictionaries
     expected = calculateExpected(frequency_filename, sigma_filename)

     log_path = os.path.join(folder_name, f"log_{curr_time}.csv")
     saveLog(windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount, frequency, expected, logPath=log_path)

for i in range(repeat):
     for windowSize in windowSizes:
          for probOfBadChannel in probOfBadChannels:
               for probOfBadNACK in probOfBadNACKs:
                    for probOfGoodNACK in probOfGoodNACKs:
                         for packetCount in packetCounts:
                              run(windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount)
                              print(f"Done with windowSize: {windowSize}, probOfBadChannel: {probOfBadChannel}, probOfBadNACK: {probOfBadNACK}, probOfGoodNACK: {probOfGoodNACK}, packetCount: {packetCount}")
