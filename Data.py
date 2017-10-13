from Tag import Tag
from DataManager import DataManager

class Data():
    word = 0
    tag = 1

    data = dict()
    organizedBigrams = dict()
    countedBigrams = dict()
    countedLabelsBigrams = dict()
    probabilityLabels = dict()
    countedWords = dict()

    dataManager = None
    probabilityWords = dict()
    tags = Tag().all()

    testData = dict()
    arrayWords = []
    arrayLabels = []

    def __init__(self, file):
        self.data = self.getSeparatedLines(file)
        self.countedWords = self.getCountedWords(self.data)
        self.organizedBigrams = self.getOrganizedBigrams(self.data)
        self.countedBigrams = self.getCountedBigrams(self.organizedBigrams)
        self.countedLabelsBigrams = self.getCountedLabelsBigrams(self.organizedBigrams)
        self.probabilityLabels = self.getProbabilityLabels(self.countedBigrams, self.countedLabelsBigrams)

    def setTest(self, file):
        self.test = self.getSeparatedLines(file)
        self.arrayWords = self.getArray(self.test, self.word)
        self.arrayLabels = self.getArray(self.test,self.tag)

    def getArray(self, dictionary, type):
        array = []
        for i in range(0,len(dictionary)):
            lineArray = []
            for bigram in dictionary[i]:
                lineArray.append(bigram[type])

            lineArray.remove(lineArray[0])
            lineArray.remove(lineArray[len(lineArray)-1])
            array.append(lineArray)

        return array

    def getSeparatedLines(self, file):
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

        return dictionary

    def getOrganizedBigrams(self, dictionary):
        bigramDictionary = dict()

        for i in range(0, len(dictionary)):
            table = []

            for j in range(0,len(dictionary[i])-1):
                value = []
                value.append(dictionary[i][j][self.tag].upper())
                value.append(dictionary[i][j + 1][self.tag].upper())
                table.append(value)

            bigramDictionary[i] = table

        return bigramDictionary

    def getCountedBigrams(self, dictionary):

        tableDictionary = dict()

        for i in range(0,len(dictionary)):
            for labels in dictionary[i]:
                key = "%s,%s" % (labels[0].upper(), labels[1].upper())
                if key in tableDictionary:
                    tableDictionary[key] = tableDictionary[key] + 1
                else:
                    tableDictionary[key] = 1

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

        return labelsDictionary

    def getProbabilityLabels(self, bigrams, labels):

        dictionary = dict()

        for bigram in bigrams:
            firstTag = bigram.split(',')[0]
            probability = bigrams[bigram]/labels[firstTag]
            key = "%s/%s" % (bigram, firstTag.upper())
            # print(key)
            # print(probability)
            dictionary[key] = probability

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

        return wordsDictionary
    #
    # def setProbTags(self):
    #     for tag in self.tags:
    #         probabilityDictionary = self.dataManager.probWordForLabel[tag]
    #         for word in probabilityDictionary:
    #             if word in self.probabilityWords:
    #                 if len(self.probabilityWords[word]) != 0:
    #                     self.probabilityWords[word][tag] = probabilityDictionary[word]
    #                 else:
    #                     self.addTagProbabily(tag, word, probabilityDictionary)
    #             else:
    #                 self.addTagProbabily(tag, word, probabilityDictionary)
    #
    #     print(self.probabilityWords)
    #
    # def addTagProbabily(self, tag, word, probabilityDictionary):
    #     dictionary = dict()
    #     dictionary[tag] = probabilityDictionary[word]
    #     self.probabilityWords[word] = dictionary

    # #{'corre': {'v': 3, 's': 5}}
    # def getProbabilityWords(self, dictionary, countedWords):
    #     wordsDictionary = dict()
    #
    #     for i in range(0, len(dictionary)):
    #         for bigram in dictionary[i]:
    #             word = bigram[self.word]
    #             tag = bigram[self.tag]
    #
    #             wordDictionary = dict()
    #             wordsDictionary[word] = wordDictionary
    #
    #     for word in wordsDictionary:
    #         for j in range(0, len(dictionary)):
    #             for bigram in dictionary[j]:
    #                 bigramWord = bigram[self.word]
    #                 label = bigram[self.tag]
    #
    #                 if bigramWord == word:
    #                     if len(wordsDictionary[word]) != 0:
    #                         if label in wordsDictionary[word]:
    #                             wordsDictionary[word][label] = wordsDictionary[word][label] + 1
    #                         else:
    #                             wordsDictionary[word][label] = 1
    #                     else:
    #                         wordsDictionary[word][label] = 1
    #
    #     for word in wordsDictionary:
    #         for label in wordsDictionary[word]:
    #             wordsDictionary[word][label] = wordsDictionary[word][label]/countedWords[word]
    #
    #     print(wordsDictionary)
    #
    #     return wordsDictionary
