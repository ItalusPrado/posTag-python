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

    word = 0
    tag = 1

    train = dict()
    test = dict()
    organizedBigrams = dict()
    countedBigrams = dict()

    def __init__(self, file):
        self.train = self.separateLines(file)
        self.organizedBigrams = self.organizeBigrams(self.train)
        self.countedBigrams = self.countBigrams(self.organizedBigrams)

    def setTest(self, test):
        self.test = test

    def separateLines(self, file):
        empty = 'empty_EMPTY'
        dictionary = dict()
        content = file.readlines()
        for i in range(0, len(content)):
            line = content[i].splitlines()

            dictionary[i] = line[0].split(' ')
            dictionary[i].append(empty)
            dictionary[i].insert(0, empty)

            array = []
            for j in range(0, len(dictionary[i])):
                word = dictionary[i][j].split('_')

                newList = []
                for w in word:
                    newList.append(w.lower())

                array.append(newList)

            dictionary[i] = array

        print(dictionary)

        return dictionary

    def organizeBigrams(self, dictionary):
        bigramDictionary = dict()

        for i in range(0, len(dictionary)):
            table = []

            for j in range(0,len(dictionary[i])-1):
                value = []
                value.append(dictionary[i][j][self.tag])
                value.append(dictionary[i][j + 1][self.tag])
                table.append(value)

            bigramDictionary[i] = table

        print(bigramDictionary)

        return bigramDictionary

    def countBigrams(self, dictionary):

        tableDictionary = dict()

        for i in range(0,len(dictionary)):
            labelDictionary = dict()

            for labels in dictionary[i]:
                key = "%s, %s" % (labels[0], labels[1])
                if key in dictionary:
                    labelDictionary[key] = labelDictionary[key] + 1
                else:
                    labelDictionary[key] = 1

            tableDictionary[i] = labelDictionary

        print(tableDictionary)

        return tableDictionary



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
