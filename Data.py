class Data():

    word = 0
    tag = 1

    data = dict()
    organizedBigrams = dict()
    countedBigrams = dict()
    countedLabelsBigrams = dict()
    probabilityLabels = dict()


    def __init__(self, file, type):
        self.data = self.getSeparatedLines(file)

        if type == 'train':
            self.organizedBigrams = self.getOrganizedBigrams(self.data)
            self.countedBigrams = self.getCountedBigrams(self.organizedBigrams)
            self.countedLabelsBigrams = self.getCountedLabelsBigrams(self.organizedBigrams)
            self.probabilityLabels = self.getProbabilityLabels(self.countedBigrams, self.countedLabelsBigrams)


    def getTestData(self):
        return self.data

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

        print(dictionary)

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

        print(tableDictionary)

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

        print(labelsDictionary)

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

        print(dictionary)

        return dictionary