class HMM():

    text = None
    word = []
    tag = []

    # P(Y/Y-1)
    probTests1 = [[0.2,0.4,0.4], # P(t/vazio)
                  [0.3,0.3,0.4], # P(t/verbo)
                  [0,5,0.1,0.4], # P(t/subs)
                  [0.1,0.6,0.2]] # P(t/prep)
    probTests2 =

    def __init__(self,text):
        self.text = text.rstrip()
        self.separateText()

    def separateText(self):
        for word in self.text.split(' '):
            separated = word.split('_')
            print(separated)
            self.word.append(separated[0])
            self.tag.append(separated[1])

