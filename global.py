BPT = []

def initializeBPT(historySize, initialValue=True):
    BPT = [initialValue for i in range(historySize)]
    print(BPT)

def getPrediction(history):
    index = getIndex(history)
    return BPT[index]

def setPrediction(prediction, history):
    index = getIndex(history)
    BPT[index] = prediction

def getIndex(history):
    index = 0
    n = 1
    for entry in range(len(history)):
        if(history[entry]):
            index += n
        n *= 2
    return index

def getBPT():
    return BPT
