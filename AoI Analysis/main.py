from AoI_of_SRARQ import AoIOfSRARQ
from calculate_AoI import calculateAoI
from save_AoI_array import saveAoIData
from save_AoI_file import saveAoIFile
from calculate_pi import calculatePi
from save_pi_dict import savePiDict
from calculate_sigma import calculateSigma
from save_sigma_dict import savePiDict
from calculate_expected import calculateExpected


windowSize = 5
probOfBadChannel= 0.2
probOfBadNACK= 0.8
probOfGoodNACK= 0.1
packetCount = 100


data = AoIOfSRARQ(windowSize,probOfBadChannel,probOfBadNACK,probOfGoodNACK,packetCount)
saveAoIData(data,"aoi_data.csv")
AoI = []
for window in data:
    AoI.append(calculateAoI(windowSize,window))

print(AoI)
saveAoIFile(AoI,"AoI.csv")

frequency = calculatePi("aoi_data.csv")
savePiDict(frequency,"frequency_data.csv")

AoIdict = calculateSigma("aoi_data.csv")
savePiDict(AoIdict,"aoi_dict.csv")

expected = calculateExpected(freqFilePath="frequency_data.csv", AoIDictFilePath="aoi_dict.csv")
print(expected)