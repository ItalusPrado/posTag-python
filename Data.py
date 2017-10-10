class Data():

    probabilityWords = dict()
    probabilityWordsLabels = dict()

    countWordLabels = dict()
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


    def countLabelForWord(self,word,label):
        if not self.countWordLabels.has_key(word):
            internDict[label] = 1
            self.countWordLabels[word] = internDict


    def probabilityForLabels(self, words, label):
        for word in words:
            probabilityLabels = dict()
            for label in labels:
                #calcular a probabilidade das labels
                probabilityLabels[label] = 0.2
            self.probabilityWordsLabels[word] = probabilityLabels
