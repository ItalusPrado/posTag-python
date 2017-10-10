class Data():

    probabilityWords = dict()
    probabilityWordsLabels = dict()
    totalWords = 0

    def addCountWord(self,word):
        self.totalWords += 1
        if not self.probabilityWords.__contains__(word):
            self.probabilityWords[word] = 1
        else:
            self.probabilityWords[word] = self.probabilityWords[word]+1


    def probForWords(self):
        for word in self.probabilityWords:
            self.probabilityWords[word] = self.probabilityWords[word]/self.totalWords


    def probabilityForLabels(self, words, labels):
        for word in words:
            probabilityLabels = dict()
            for label in labels:
                #calcular a probabilidade das labels
                probabilityLabels[label] = 0.2
            self.probabilityWordsLabels[word] = probabilityLabels
