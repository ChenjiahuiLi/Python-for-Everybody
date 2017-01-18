from numpy import *
import operator
from os import listdir

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels= array(['A','A','B','B'])
    return group, labels

## Part 1: idealized KNN
def classify0(inX, dataSet, labels, k):
    # numpy.narray.shape: return a tuple of array dimension
    dataSetSize = dataSet.shape(0)
    # numpy.tile(A,reps): return an array by constucting A reps number of times
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    # square every entry in the diffMat array
    sqDiffMat = diffMat ** 2
    # sum along the row, leave a column of row sum
    sqDistances = sqDiffMat.sum(axis = 1)
    # square root of every entry in the sqDistances matrix
    distances = sqDistances**0.5
    # Since we want the smallest distances
    # sort entries in distances in ascending order, take the sorted indicis
    sortedDistIndicis = distances.argsort()
    classCount={}
    for i in range(k):
        # take the label correspond to the ith smallest distances
        voteIlabel = labels[sortedDistIndicis[i]]
        # dict.get(key,0): return 0 in case the key not yet exist in the dictionary
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True) # descending:big,small
    return sortedClassCount

## Part 2: parsing data from text file
def file2matrix(filename):
   fr = open(filename)
   arrayOLines = fr.readlines()
   numberOLines = len(arrayOLines)
   returnMat = zeros((numberOLines,3))
   classLabelVector = []
   index = 0
   for line in arrayOLines:
       """
       First use strip() remove the heading and tailing spaces
       Second use split() to split each line(string) by '\t'
       """
       line = line.strip()
       listFromLine = line.split('\t')
       returnMat[index,:] = listFromLine[0:3]
       classLabelVector.append(int(listFromLine[-1]))
       index += 1
    return returnMat, classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0) # return a row vector containing column min
    #print minVals
    maxVals = dataSet.max(0) # return a row vector containing column max
    #print maxVals
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals

# Part 3: test accuracy

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))

# Part 4:Putting together a useful system and Make prediction
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percenTats = float(raw_input('Percentage of time spend playing video game?'))
    ffMiles = float(raw_input('Frequent flier miles earned per year?'))
    iceCream = float(raw_input('liters of ice cream consume per year?'))
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percenTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    print "You will probably like this person: ", resultList[classifierResult - 1]

# Part 5:  Example a handwriting recognition system
def findDigitNum(filename):
    fr = open(filename)
    num = 0
    colnum = len(fr.readlines())
    fr = open(filename)
    for line in fr.readlines():
        line = line.strip()
        #print line
        listFromLine = line.split('')
        #print listFromLine
        num += len(listFromLine)
        #print num
    return num

def img2vector(filename):
    fr = open(filename)
    returnVector = zeros((1,1024))
    for i in range(32):
        lineStr = fr.readlines()
        for j in range(32):
            returnVector[0,32*i+j] = int(lineStr[j])
    return returnVector

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]  # since the filename, eg.'2_108.txt', contains the labels of the image
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print 'the classifier came back with: %d, the real answer is: %d' % (classifierResult,classNumStr)
        if(classifierResult != classNumstr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))




