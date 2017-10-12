class Node():

    father = None
    tag = None
    currentValue = None
    depth = None

    def __init__(self,father,tag,value,cumulated,probWordGivenLabel,depth):
        self.father = father
        self.tag = tag
        self.currentValue = value*cumulated*probWordGivenLabel
        self.depth = depth

    def expand(self,tag,value):
        node = Node(self,tag,value,self.currentValue)
        return node