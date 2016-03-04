from LoadFiles import load
from ID3Tree import ID3Tree
from pprint import pprint

import math



d = {0: [1,2,3,4,5,6,7],
     1: [1,2,3,4,5,6],
     2: [1,2,3,4],
     3: [1,2],
     4: [1,2,3],
     5: [1,2,3],
     6: [1,2],
     7: [1,2],
     8: [1,2],
     9: [1,2]}

bestAttr = [9,5,8,4,7,6,3,1,2,0]

bestAttrName = ["Code for class", "Code for largest spot size",
                "Code for spot distribution", "Activity",
                "Evolution"," Previous 24 hour flare activity code",
                "Historically-complex","Did region become historically complex on this pass across the sun's disk ",
                "Area", "Area of the largest spot"]

def main():
    mat = load("flaredata2.txt")
    
    tree = recurtion_function(mat, 0)
    
    pprint(tree)
    
    ##InformationGain(mat,0)
    ##recurtion_function(matList)



## new to make sub lists based off attrubutes and then use recurtion to get the enropy
##    python -m pdb myscript.py






def testAllSameClass(mat):
    c = getClass(mat[0])
    for i in range(len(mat)):
        if(getClass(mat[i]) != c):
            return False

    return True
        
def getClass(array):
    if(array[10]  != 0 and array[11] == 0 and array[12] == 0):
        return 1
    elif(array[10]  == 0 and array[11] != 0 and array[12] == 0):
        return 2
    elif(array[10]  == 0 and array[11] == 0 and array[12] != 0):
        return 3
    else:
        return 4
    



def mostComman(mat):
    cCl = 0
    mCl = 0
    xCl = 0
    noCl = 0
    for i in range(len(mat)):
        tempClass = getClass(mat[i])
        if( tempClass == 1):
            cCl = cCl + 1
        elif(tempClass == 2):
            mCl = mCl + 1 
        elif(tempClass == 3):
            xCl = xCl + 1
        else:
            noCl = noCl + 1
    maxNum = max(cCl, mCl, xCl, noCl)
    if(maxNum == cCl):
        return "C-class"
    elif(maxNum == mCl):
        return "M-class"
    elif(maxNum == xCl):
        return "X-class"
    else:
        return "Nall-Class"
    
    
def allSame(mat):
    test = getClass(mat[0])
    if(test == 1):
        return "C-class"
    elif(test == 2):
        return "M-class"
    elif(test == 3):
        return "X-class"
    else:
        return "Nall-Class"

def recurtion_function(mat,attr):
        print(attr)
        root = ID3Tree("Node",mat)
        if(testAllSameClass(mat)):
            root.setLable(allSame(mat))
        elif(len(bestAttr) == 0):
            root.setLable(mostComman(mat))
        else:
            
            A = bestAttr.pop()
            root.setLable(bestAttrName[A])
            print("this is attr " + str(A))
            for x in d.get(A):
               print("this is x = " + str(x))
               sub = makeSublist(mat,A,x)
            
                #if(len(sub) == 0):
               root.addToTree(str(x),sub)
               if(len(root.childern[x-1].sublist) == 0):
                   root.setLable(mostComman(mat))
               else:
                 print("recution case")
                 recurtion_function(sub,attr+1)
        return root
                   

                
                

            

            
            
        
        
def printSub(sub):
    for i in range(len(sub)):
        print(sub[i])
    



def InformationGain(mat, attr):
    if attr <10:
        print("#######################################################################")
        parentEntr = entropy(mat)
        print("Entropy of the parent --- >" + str(parentEntr))
        kidEntrSum = 0
        ##print(parentEntr)
        
        for x in d.get(attr):

            sub = makeSublist(mat,attr,x)
            #print("entro = " + str(entropy(sub)))

            kidEntrSum = kidEntrSum + ((len(sub)/len(mat))*entropy(sub))

        print("from this split ---> " + str(parentEntr - kidEntrSum))
        InformationGain(mat,attr+1)


def makeSublist(mat, attr, key):
    sub = []
    
    
    for i in range(len(mat)):
            if mat[i][attr] == key and checkIfmore(mat[i]):
                sub.append(mat[i])
    
    return sub



def checkIfmore(lis):
    count = 0
    if lis[10] != 0:
        count = count +1
    if lis[11] != 0:
        count = count +1
    if lis[12] != 0:
        count = count +1
    if(count <= 1):
        return True
    else:
        return False



def entropy( mat):
    if (len(mat) !=0):
        entNum = 0.0
        entrFrac = 0.0
        for i   in range(3):
            
            entrFrac = (countClass(mat,i+10)/len(mat))
            if(entrFrac != 0):
                entNum = entNum - (entrFrac * math.log(entrFrac,2))
            else:
                enentNum = entNum - 0
        entrFrac = (countNoClass(mat)/len(mat))
        entNum = entNum - (entrFrac * math.log(entrFrac,2))
        
        
        return entNum
    else:
        return 0
    
def countClass(mat, attr):
    count = 0
    for i in range(len(mat)):
        if(mat[i][attr] != 0):
            count = count + 1
    ##print("in count class = " + str(count))
    return count
    
def countNoClass(mat):
    count = 0
    for i in range(len(mat)):
        if(mat[i][10] == 0 and mat[i][11] == 0 and mat[i][12] == 0):
            count = count + 1
            
    ##print("in other class = " + str(count))
    return count
    



##print(clf.predict([2,2]))
##clf.predict([2,2])

main()




