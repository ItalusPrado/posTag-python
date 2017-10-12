from Node import Node
from DataManager import DataManager
from Tag import Tag

class HMM():

    text = None
    data = dict()
    word = []
    tag = []
    board = []
    path = []

    tags = Tag().all()

    probTests1 = [[0.2,0.4,0.4], # P(t/vazio)
                  [0.3,0.5,0.2], # P(t/verbo)
                  [0.5,0.1,0.4], # P(t/subs)
                  [0.1,0.6,0.2]] # P(t/prep)

    probTests2 = [[0.0,0.7,0.3], # Palavra Ela = verbo 0.0 ; subs 0.7 ; prep 0.3
                  [0.6,0.2,0.2]] # Palavra Corre = verbo 0.6 ; subs 0.2 ; prep 0.2

    probabilityWords = dict()

    def __init__(self,text):
        self.text = text
        # self.separateText()

    def separateText(self):
        for word in self.text.split(' '):
            separated = word.split('_')
            print(separated)
            self.word.append(separated[0])
            self.tag.append(separated[1])

    def startSearch(self):
        node = Node(None,self.tags[0],1,1,1,0)
        self.board.append(node)
        self.expandTree()

    def expandTree(self):
        index = None
        value = None
        for node in range(0,len(self.board)):
            print("Borda", self.board[node].currentValue)
            if node == 0:
                index = 0
                value = self.board[node].currentValue
            else:
                if self.board[node].currentValue > value:
                    index = node
                    value = self.board[node].currentValue

        actualNode = self.board[index]
        del self.board[index]
        # print(actualNode.tag)
        # print(self.tags.index(actualNode.tag))

        a = 0
        print("--- Atual ---", actualNode.currentValue, actualNode.tag)
        if actualNode.depth < len(self.word):
            for prob in self.probTests1[self.tags.index(actualNode.tag)]:
                newNode = Node(actualNode,self.tags[a+1],prob,actualNode.currentValue,self.probTests2[actualNode.depth][a],actualNode.depth+1)
                self.board.append(newNode)
                a = a+1
            self.expandTree()
        else:
            while True:
                self.path.append(actualNode)
                if actualNode.father == None:
                    break
                actualNode = actualNode.father
            print("Caminho")
            for tagging in self.path:
                print(tagging.tag)