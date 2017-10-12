class Node():

    father = None
    tag = None
    currentValue = None
    depth = None

    def __init__(self,father,tag,value,cumulated,depth):
        self.father = father
        self.tag = tag
        self.currentValue = value*cumulated
        self.depth = depth

    def expand(self,tag,value):
        node = Node(self,tag,value,self.currentValue)
        return node