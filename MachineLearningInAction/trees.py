def createDataSet():
    dataSet = [
        [1,1,'yes'],
        [1,1,'yes'],
        [1,0,'no'],
        [0,1,'no'],
        [0,1,'no']
    ]
    labels = ['no surfacing','flippers']
    return dataSet, labels

# Program 3-1 Calculate Shannon Entropy
from math import log
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVect in dataSet:
        currentLabel = featVect[-1]
        labelCounts[currentLabel] = labelCounts.get(currentLabel,0) + 1
    shannonEnt = 0.0
    for label in labelCounts:
        prob = labelCounts.get(label) / float(numEntries)
        shannonEnt -= prob*log(prob,2)
    return labelCounts, shannonEnt

# Program 3-2 Split dataset based on a certain feature
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVect in dataSet:
        if featVect[axis] == value:
            reducedFeatVec = featVect[:axis]
            reducedFeatVec.extend(featVect[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
# Part 3: Choosing the best feature to split on
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1 # since 1 is for label
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList) # set() get the unorderd collection of unique elements in featList
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classList.key():
            classCount[vote]=0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(), reverse = True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat,value), subLabels)
    return myTree

