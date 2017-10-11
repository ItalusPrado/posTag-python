class Data():

    probabilityWords = dict()
    probabilityWordsLabels = dict()

    countWordLabels = dict()
    bigrams = dict()

    countWordForLabel = dict() # Contagem de P(X/Y)
    probabilityWordForLabel = dict() # Probabilidade de P(X/Y)

    totalWords = 0

    def setCountAndProbForLabel(self):
        for word in self.train:
            self.setCountForLabel(word[0],word[1])
        self.setProbForLabel()


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

    train = []
    test = []

    countLabels = dict()

    def __init__(self, file):
        self.train = self.separateLines(file)
        self.countLabels = self.createCountLabels(self.train)

    def setTest(self, test):
        self.test = test

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
                    array.append(final)

        return array

    def createCountLabels(self, array):
        tag = 1
        table = []
        for i in range(0, len(array)-1):
            value = []
            value.append(array[i][tag])
            value.append(array[i + 1][tag])
            table.append(value)

        dictionary = dict()
        for labels in table:
            key = "%s, %s" % (labels[0], labels[1])
            if key in dictionary:
                dictionary[key] = dictionary[key] + 1
            else:
                dictionary[key] = 1

        return dictionary


#################### ANTIGO TUDO QUE ESTÁ ABAIXO #################

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
