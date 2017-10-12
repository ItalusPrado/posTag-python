class DataManager():

    train = []
    countWordForLabel = dict() # Contagem de P(X/Y)
    probWordForLabel = dict() # Probabilidade de P(X/Y)

    def __init__(self, file):
        self.data = self.separateLines(file)

    def separateLines(self, file):
        array = []
        content = file.readlines()
        for i in range(0, len(content)):
            line = content[i].splitlines()
            for j in range(0, len(line)):
                word = line[j].split(' ')
                for h in range(0, len(word)):
                    final = word[h].split('_')
                    final[0] = final[0].lower()
                    final[1] = final[1].lower()
                    array.append(final)

        return array

    def setCountAndProbForLabel(self):
        for word in self.data:
           self.setCountForLabel(word[0], word[1])

        self.setProbForLabel()

    def setCountForLabel(self, word, label):

        if label in self.countWordForLabel:

            if word in self.countWordForLabel[label]:
                self.countWordForLabel[label][word] = self.countWordForLabel[label][word] + 1
            else:
                self.countWordForLabel[label][word] = 1
        else:
            self.countWordForLabel[label] = {word: 1}

    def setProbForLabel(self):

        for label in self.countWordForLabel:
            total = 0
            for word in self.countWordForLabel[label]:
                total += self.countWordForLabel[label][word]

            for word in self.countWordForLabel[label]:
                if label in self.probWordForLabel:
                    self.probWordForLabel[label][word] = self.countWordForLabel[label][word] / total
                else:
                    self.probWordForLabel[label] = {word: self.countWordForLabel[label][word] / total}

