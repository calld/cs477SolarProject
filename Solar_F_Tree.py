from LoadFiles import load
import pypi
import math



d = {0: [0,1,2,3,4,5,6],
     1: [0,1,2,3,4,5],
     2: [0,1,2,3],
     3: [1,2],
     4: [1,2,3],
     5: [1,2,3],
     6: [1,2],
     7: [1,2],
     8: [1,2],
     9: [1,2]}



def main():
    mat = load("flaredata2.txt")

    InformationGain(mat,0)
    ##recurtion_function(matList)



## new to make sub lists based off attrubutes and then use recurtion to get the enropy


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
    

class ID3Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
main()



test = Tree()
print(test.data)




