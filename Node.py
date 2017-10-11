class Node():

    father = None
    tag = None
    currentValue = None

    def __init__(self,father,tag,value,cumulated):
        self.father = father
        self.tag = tag
        self.currentValue = value*cumulated

    def expand(self,tag,value):
        node = Node(self,tag,value,self.currentValue)
        return node