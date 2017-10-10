from Data import Data

train = open("train2.txt", encoding="utf8")
database = Data(train)

print(database.train)
print(database.countLabels)

################### NÃO SEI MAIS NADA AÍ DEBAIXO ######################

def setProbWord(file):
    for text in file:
        words = text.split(' ')
        for word in words:
            separated = word.split('_')
            database.addCountWord(separated[0].lower())

def setLabelCount(file):
    for text in file:
        words = text.split(' ')
        for word in words:
            separated = word.split('_')
            database.countLabelForWord(separated[0].lower(),separated[1].lower())

def chooseBigramFromText(file):
    for text in file:
        words = text.split(' ')
        for wordNumber in range(0 , len(words)):
            separated = words[wordNumber].split('_')
            if wordNumber == 0:
                print(separated[0], separated[1], "empty")
            else:
                lastWord = words[wordNumber-1].split('_')
                print(separated[0], separated[1], lastWord[1])
