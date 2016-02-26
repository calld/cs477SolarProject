from math import sqrt

def firstField(val):
    if (val == "A"):
        return 0
    elif(val == "B"):
        return 1
    elif(val == "C"):
        return 2
    elif(val == "D"):
        return 3
    elif(val == "E"):
        return 4
    elif(val == "F"):
        return 5
    elif(val == "H"):
        return 6

def secondField(val):
    if (val == "X"):
        return 0
    elif (val == "R"):
        return 1
    elif (val == "S"):
        return 2
    elif (val == "A"):
        return 3
    elif (val == "H"):
        return 4
    elif (val == "K"):
        return 5

def thirdField(val):
    if (val == "X"):
        return 0
    elif (val == "O"):
        return 1
    elif (val == "I"):
        return 2
    elif (val == "C"):
        return 3

def convert(value, indx):
    if (indx == 0):
        return firstField(value)
    elif(indx == 1):
        return secondField(value)
    elif(indx == 2):
        return thirdField(value)
    else:
        return int(value)

def load(filename):
    raw = open(filename, 'r')
    raw.readline()
    data = [[line[x] for x in range(0, 25, 2)] for line in raw.readlines()]
    numericdata = [[convert(ele[x], x) for x in range(len(ele))] for ele in data]
    return numericdata

def dist(first, second):
    SSD = 0
    for i in range(len(first)):
        SSD = SSD + (first[i] - second[i])**2
    return sqrt(SSD)
