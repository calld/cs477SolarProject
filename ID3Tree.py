class ID3Tree():

    def __init__(self,lable, childern = []):
      self.lable = lable
      self.childern = childern


    def addToTree(self, lable, sublist):
        branch = ID3Tree(lable,sublist)
        self.childern.append(branch)
        


mat = [1,2,3]
tat = []

tree = ID3Tree("test",tat)
tree.addToTree("this",mat)
print(tree.childern[0].lable)
