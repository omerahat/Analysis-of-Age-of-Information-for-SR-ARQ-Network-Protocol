from AoI_of_SRARQ import AoIOfSRARQ
from calculate_AoI import calculateAoI
from save_AoI_array import saveAoIData
from write_AoI_file import writeAoIFile

windowSize = 3
probOfNACK = 0.1
packetCount = 4000

data = AoIOfSRARQ(windowSize,probOfNACK,packetCount)
saveAoIData(data,"aoi_data.csv")
AoI = []
for window in data:
    AoI.append(calculateAoI(windowSize,window))

print(AoI)
writeAoIFile(AoI,"AoI.csv")