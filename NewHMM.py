from Node import Node

class NewHMM():

    text = None
    # data = dict()
    word = []
    tag = []
    board = []
    path = []

    wordToTest = ["eu","quero","passar","professor","me","deixa","passar"]
    tags = ['pcp','pden','cur','prep','prep+prosub','ks','adv-ks','prep+adv','pro-ks','num','prosub','adv','proadj','nprop','pu','propess','prep+art','adj','v','n','art','prep+propess','in','prep+pro-ks','prep+proadj','kc']

    probYforY = None
    probXforY = None

    def __init__(self,probxy,probyy):
        self.probXforY = probxy
        self.probYforY = probyy

    def separateText(self):
        for word in self.text.split(' '):
            separated = word.split('_')
            print(separated)
            self.word.append(separated[0])
            self.tag.append(separated[1])

    def startSearch(self):
        node = Node(None,'empty',1,1,1,0)
        self.board.append(node)
        self.expandTree2()

    def expandTree2(self):
        index = None
        value = None
        for node in range(0, len(self.board)):
            if node == 0:
                index = 0
                value = self.board[node].currentValue
            else:
                if self.board[node].currentValue > value:
                    index = node
                    value = self.board[node].currentValue

        actualNode = self.board[index]
        del self.board[index]
        a = 0
        if actualNode.depth < len(self.wordToTest):
            for tag in self.tags:
                key = "%s,%s/%s" % (actualNode.tag.upper(), tag.upper(), actualNode.tag.upper())
                if self.wordToTest[actualNode.depth] in self.probXforY[tag] and key in self.probYforY :
                    newNode = Node(actualNode, tag, self.probYforY[key], actualNode.currentValue,self.probXforY[tag][self.wordToTest[actualNode.depth]], actualNode.depth + 1)
                    self.board.append(newNode)
            self.expandTree2()
        else:
            while True:
                self.path.append(actualNode)
                if actualNode.father == None:
                    break
                actualNode = actualNode.father
            self.path.pop()

            for word in self.wordToTest:
                print(word, end=' ')
            print()
            for tagging in reversed(self.path):
                print(tagging.tag, end=' ')



    # def expandTree(self):
    #     index = None
    #     value = None
    #     for node in range(0,len(self.board)):
    #         print("Borda", self.board[node].currentValue)
    #         if node == 0:
    #             index = 0
    #             value = self.board[node].currentValue
    #         else:
    #             if self.board[node].currentValue > value:
    #                 index = node
    #                 value = self.board[node].currentValue
    #
    #     actualNode = self.board[index]
    #     del self.board[index]
    #
    #
    #
    #     a = 0
    #     print("--- Atual ---", actualNode.currentValue, actualNode.tag)
    #     if actualNode.depth < len(self.word):
    #         for prob in self.probTests1[self.tags.index(actualNode.tag)]:
    #             newNode = Node(actualNode,self.tags[a+1],prob,actualNode.currentValue,self.probXforY[][actualNode.depth],actualNode.depth+1)
    #             self.board.append(newNode)
    #             a = a+1
    #         self.expandTree()
    #     else:
    #         while True:
    #             self.path.append(actualNode)
    #             if actualNode.father == None:
    #                 break
    #             actualNode = actualNode.father
    #         print("Caminho")
    #         for tagging in self.path:
    #             print(tagging.tag)