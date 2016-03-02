class ID3Tree():

    def __init__(self,lable, sublist = []):
      childern = []
      self.lable = lable
      self.sublist = sublist
      self.childern = childern


    def addToTree(self, lable, sublist):
        branch = ID3Tree(lable,sublist)
        self.childern.append(branch)

    def setLable(self, lable):
        self.lable = lable
        
        
    
