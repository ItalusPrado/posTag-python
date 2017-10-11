class Data():

    probabilityWords = dict()
    probabilityWordsLabels = dict()

    countWordLabels = dict()
    bigrams = dict()

    countWordForLabel = dict() # Contagem de P(X/Y)
    probabilityWordForLabel = dict() # Probabilidade de P(X/Y)

    totalWords = 0

    def setCountForLabel(self,word,label):
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
                if label in self.probabilityWordForLabel:
                        self.probabilityWordForLabel[label][word] = self.countWordForLabel[label][word]/total
                else:
                    self.probabilityWordForLabel[label] = {word : self.countWordForLabel[label][word]/total}

    # ---------------------------- DAQUI PRA BAIXO TÁ ERRADO -----------------------


    # Talvez seja inutil
    def addCountWord(self,word):
        self.totalWords += 1
        if not self.probabilityWords.__contains__(word):
            self.probabilityWords[word] = 1
        else:
            self.probabilityWords[word] = self.probabilityWords[word]+1

    # Talvez seja inutil
    def probForWords(self):
        for word in self.probabilityWords:
            self.probabilityWords[word] = self.probabilityWords[word]/self.totalWords


    def countLabelForWord(self,word,label):
        if word in self.countWordLabels:
            if label in self.countWordLabels[word]:
                self.countWordLabels[word][label] = self.countWordLabels[word][label]+1
            else:
                self.countWordLabels[word][label] = 1
        else:
            self.countWordLabels[word] = {label: 1}

    def probabilityLabelForWord(self):
        for word in self.countWordLabels:
            total = self.probabilityWords[word]
            for label in self.countWordLabels[word]:
                if word in self.probabilityWordsLabels:
                        self.probabilityWordsLabels[word][label] = self.countWordLabels[word][label]/total
                else:
                    self.probabilityWordsLabels[word] = {label: self.countWordLabels[word][label]/total}

    def createBigrams(self,word,labelWord,previousLabel):

        print("batata")


    def printBigram(self,word,labelWord,previousLabel):
        print(word,labelWord,previousLabel)


    # def viterbi(self,sentence):
    #     words = sentence.split(' ')
    #     for word in words:




    # def probabilityForLabels(self, words, label):
    #     for word in words:
    #         probabilityLabels = dict()
    #         for label in labels:
    #             #calcular a probabilidade das labels
    #             probabilityLabels[label] = 0.2
    #         self.probabilityWordsLabels[word] = probabilityLabels
