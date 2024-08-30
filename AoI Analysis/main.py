from AoI_of_SRARQ import AoIOfSRARQ
from calculate_AoI import calculateAoI
from save_AoI_array import saveAoIArray
from save_AoI_file import saveAoIFile
from calculate_pi import calculatePi
from save_pi_dict import savePiDict
from calculate_sigma import calculateSigma
from save_sigma_dict import savePiDict
from calculate_expected import calculateExpected
from save_log import saveLog
import time
import os


repeat = 1
windowSizes = [2,3,4,5,6,7,8,9]
probOfBadChannels = [0.01,0.02,0.05,0.1,0.2]
probOfBadNACKs = [0.7,0.8,0.9] 
probOfGoodNACKs = [0.01,0.05,0.1,0.15,0.2] 
packetCounts = [100,1000,10000,100000,1000000]

def run(windowSize,probOfBadChannel,probOfBadNACK,probOfGoodNACK,packetCount):
    """
    Run the SR ARQ simulation and save results for given parameters.

    :param windowSize: Size of the window.
    :param probOfBadChannel: Probability of a bad channel.
    :param probOfBadNACK: Probability of a bad NACK.
    :param probOfGoodNACK: Probability of a good NACK.
    :param packetCount: Number of packets in the simulation.
    """
    # create new folder
    curr_time = time.strftime("%H:%M:%S")
    folder_name = curr_time
    os.mkdir(folder_name)
    os.chdir(folder_name)
    
    #create parameters file
    with open("parameters.txt", "w") as f:
        f.write(f"repeat: {repeat}\n")
        f.write(f"windowSize: {windowSizes}\n")
        f.write(f"probOfBadChannel: {probOfBadChannels}\n")
        f.write(f"probOfBadNACK: {probOfBadNACKs}\n")
        f.write(f"probOfGoodNACK: {probOfGoodNACKs}\n")
        f.write(f"packetCount: {packetCounts}\n")


    data = AoIOfSRARQ(windowSize,probOfBadChannel,probOfBadNACK,probOfGoodNACK,packetCount)
    saveAoIArray(data,"aoi_data.csv")
    AoI = []
    for window in data:
        AoI.append(calculateAoI(windowSize,window))


    saveAoIFile(AoI,"AoI.csv")

    frequency = calculatePi("aoi_data.csv")
    savePiDict(frequency,"frequency_data2.csv")

    AoIdict = calculateSigma("aoi_data.csv")
    savePiDict(AoIdict,"aoi_dict2.csv")

    expected = calculateExpected(freqFilePath="frequency_data2.csv", AoIDictFilePath="aoi_dict2.csv")

    saveLog(windowSize, probOfBadChannel, probOfBadNACK, probOfGoodNACK, packetCount, frequency, expected,logPath="log2.csv")

for i in range(repeat):
    for windowSize in windowSizes:
        for probOfBadChannel in probOfBadChannels:
            for probOfBadNACK in probOfBadNACKs:
                for probOfGoodNACK in probOfGoodNACKs:
                    for packetCount in packetCounts:
                        run(windowSize,probOfBadChannel,probOfBadNACK,probOfGoodNACK,packetCount)
                        print("Done with windowSize: ",windowSize," probOfBadChannel: ",probOfBadChannel," probOfBadNACK: ",probOfBadNACK," probOfGoodNACK: ",probOfGoodNACK," packetCount: ",packetCount)
