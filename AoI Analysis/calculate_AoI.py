from get_all_indexes import getAllIndexes

def calculateAoI(windowSize,window):
    v = max(window)
    j0 = min(getAllIndexes(v,window))
    j1 = max(getAllIndexes(v,window))
    m = windowSize
    if v > 0:
        return m * (v-1) + j1 + 1
    else:
        return j0 - m * v