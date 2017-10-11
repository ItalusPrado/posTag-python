from Data import Data
from HMM import HMM

train = open("train2.txt", encoding="utf8")
test = open("test.txt",encoding="utf8")
database = Data(train)
# database.separateLines(train)
print(database.countedBigrams)

text = test.readlines()[0]
print(text)

hmm = HMM(text)
# database.setCountAndProbForLabel()
# print(database.countLabels)

################### NÃO SEI MAIS NADA AÍ DEBAIXO ######################


# def setProbWord(file):
#     for text in file:
#         words = text.split(' ')
#         for word in words:
#             separated = word.split('_')
#             database.addCountWord(separated[0].lower())
#
# def setLabelCount(file):
#     for text in file:
#         words = text.split(' ')
#         for word in words:
#             separated = word.split('_')
#             database.countLabelForWord(separated[0].lower(),separated[1].lower())
#
# def chooseBigramFromText(file):
#     for text in file:
#         words = text.split(' ')
#         for wordNumber in range(0 , len(words)):
#             separated = words[wordNumber].split('_')
#             if wordNumber == 0:
#                 database.createBigrams(separated[0], separated[1], "empty")
#             else:
#                 lastWord = words[wordNumber-1].split('_')
#                 database.createBigrams(separated[0], separated[1], lastWord[1])




# database.separateLines(train) # Separando arquivo
# setWordProbForLabel(database.train) # Calculando P(X / Y)
# database.setProbForLabel()
#
#
# print(database.countWordForLabel)
# print(database.probabilityWordForLabel)

# setProbWord(trainTexts) # Calculando a contagem de cada palavra (pode ser útil)
# setLabelCount(trainTexts) # Calculando a contagem das labels de cada palavra
# # database.probabilityLabelForWord()
# # chooseBigramFromText(trainTexts)
# # print(database.probabilityWordsLabels["a"])
# # print(database.countWordLabels['jersei'])
# # print(len(database.countWordLabels))

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