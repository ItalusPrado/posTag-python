class Data():
    probabilityWords = dict()
    probabilityWordsLabels = dict()

    countWordLabels = dict()
    bigrams = dict()

    countWordForLabel = dict()  # Contagem de P(X/Y)
    probabilityWordForLabel = dict()  # Probabilidade de P(X/Y)

    totalWords = 0

    def setCountAndProbForLabel(self):
        for word in self.train:
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
                if label in self.probabilityWordForLabel:
                    self.probabilityWordForLabel[label][word] = self.countWordForLabel[label][word] / total
                else:
                    self.probabilityWordForLabel[label] = {word: self.countWordForLabel[label][word] / total}

    word = 0
    tag = 1

    data = dict()
    organizedBigrams = dict()
    countedBigrams = dict()
    countedLabelsBigrams = dict()
    probabilityLabels = dict()
    countedWords = dict()
    probabilityWords = dict()

    def __init__(self, file, type):
        self.data = self.getSeparatedLines(file, type)

        if type == 'test':
            self.countedWords = self.getCountedWords(self.data)
            self.probabilityWords = self.getProbabilityWords(self.data,self.countedWords)

        if type == 'train':
            self.organizedBigrams = self.getOrganizedBigrams(self.data)
            self.countedBigrams = self.getCountedBigrams(self.organizedBigrams)
            self.countedLabelsBigrams = self.getCountedLabelsBigrams(self.organizedBigrams)
            self.probabilityLabels = self.getProbabilityLabels(self.countedBigrams, self.countedLabelsBigrams)


    def getTestData(self):
        return self.data

    def getSeparatedLines(self, file, type):
        empty = 'empty_EMPTY'
        dictionary = dict()
        content = file.readlines()
        for i in range(0, len(content)):
            line = content[i].splitlines()

            dictionary[i] = line[0].split(' ')
            if type == 'train':
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

        # print(dictionary)

        return dictionary

    def getOrganizedBigrams(self, dictionary):
        bigramDictionary = dict()

        for i in range(0, len(dictionary)):
            table = []

            for j in range(0,len(dictionary[i])-1):
                value = []
                value.append(dictionary[i][j][self.tag])
                value.append(dictionary[i][j + 1][self.tag])
                table.append(value)

            bigramDictionary[i] = table

        return bigramDictionary

    def getCountedBigrams(self, dictionary):

        tableDictionary = dict()

        for i in range(0,len(dictionary)):
            for labels in dictionary[i]:
                key = "%s, %s" % (labels[0], labels[1])
                if key in tableDictionary:
                    tableDictionary[key] = tableDictionary[key] + 1
                else:
                    tableDictionary[key] = 1

        # print(tableDictionary)

        return tableDictionary

    def getCountedLabelsBigrams(self, dictionary):

        labelsDictionary = dict()

        for i in range(0,len(dictionary)):
            for labels in dictionary[i]:
                firstTag = labels[0]
                if firstTag in labelsDictionary:
                    labelsDictionary[firstTag] = labelsDictionary[firstTag] + 1
                else:
                    labelsDictionary[firstTag] = 1

        # print(labelsDictionary)

        return labelsDictionary

    def getProbabilityLabels(self, bigrams, labels):

        dictionary = dict()

        for bigram in bigrams:
            firstTag = bigram.split(',')[0]
            probability = bigrams[bigram]/labels[firstTag]
            key = "%s / %s" % (bigram, firstTag)
            # print(key)
            # print(probability)
            dictionary[key] = probability

        # print(dictionary)

        return dictionary

    def getCountedWords(self,dictionary):
        wordsDictionary = dict()

        for i in range(0, len(dictionary)):
            for bigram in dictionary[i]:
                word = bigram[self.word]

                if word in wordsDictionary:
                    wordsDictionary[word] = wordsDictionary[word] + 1
                else:
                    wordsDictionary[word] = 1

        # print(wordsDictionary)

        return wordsDictionary

    # #{'corre': {'v': 3, 's': 5}}
    def getProbabilityWords(self, dictionary, countedWords):
        wordsDictionary = dict()

        for i in range(0, len(dictionary)):
            for bigram in dictionary[i]:
                word = bigram[self.word]
                tag = bigram[self.tag]

                wordDictionary = dict()
                wordsDictionary[word] = wordDictionary

        for word in wordsDictionary:
            for j in range(0, len(dictionary)):
                for bigram in dictionary[j]:
                    bigramWord = bigram[self.word]
                    label = bigram[self.tag]

                    if bigramWord == word:
                        if len(wordsDictionary[word]) != 0:
                            if label in wordsDictionary[word]:
                                wordsDictionary[word][label] = wordsDictionary[word][label] + 1
                            else:
                                wordsDictionary[word][label] = 1
                        else:
                            wordsDictionary[word][label] = 1

        for word in wordsDictionary:
            for label in wordsDictionary[word]:
                wordsDictionary[word][label] = wordsDictionary[word][label]/countedWords[word]

        print(wordsDictionary)

        return wordsDictionary
