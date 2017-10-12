from Node import Node

class HMM():

    text = None
    word = []
    tag = []
    board = []
    path = []

    tags = ["Empty","V","Subs","Prepo"]

    probTests1 = [[0.2,0.4,0.4], # P(t/vazio)
                  [0.3,0.5,0.2], # P(t/verbo)
                  [0.5,0.1,0.4], # P(t/subs)
                  [0.1,0.6,0.2]] # P(t/prep)

    probTests2 = [[0.0,0.7,0.3], # Palavra 1 = verbo 0.0 ; subs 0.7 ; prep 0.3
                  [0.6,0.2,0.2]] # Palavra 1 = verbo 0.6 ; subs 0.2 ; prep 0.2

    def __init__(self,text):
        self.text = "ela_N corre_V" #text.rstrip()
        self.separateText()

    def separateText(self):
        for word in self.text.split(' '):
            separated = word.split('_')
            print(separated)
            self.word.append(separated[0])
            self.tag.append(separated[1])

    def startSearch(self):
        node = Node(None,self.tags[0],1,1,0)
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
        # if actualNode.father == None:
        #     print(actualNode.tag, actualNode.depth, "empty")
        # else:
        #     print(actualNode.tag, actualNode.depth, actualNode.father.tag)
        if actualNode.depth < len(self.word):
            for prob in self.probTests1[self.tags.index(actualNode.tag)]:
                newNode = Node(actualNode,self.tags[a+1],prob,actualNode.currentValue,actualNode.depth+1)
                self.board.append(newNode)
                a = a+1
            self.expandTree()
        else:
            while True:
                self.path.append(actualNode)
                if actualNode.father == None:
                    break
                actualNode = actualNode.father
            for tagging in self.path:
                print(tagging.tag)


