from Node import Node

class HMM():

    text = None
    word = []
    tag = []
    nodes = []

    tags = ["Empty","V","Subs","N"]

    probTests1 = [[0.2,0.4,0.4], # P(t/vazio)
                  [0.3,0.3,0.4], # P(t/verbo)
                  [0,5,0.1,0.4], # P(t/subs)
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
        node = Node(None,self.tag[0],1,1)
        for index in range(0,len(self.probTests1[0])):
            


