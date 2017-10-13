from Data import Data
from DataManager import DataManager
from NewHMM import NewHMM

train = open("train.txt", encoding="utf8")
data = Data(train)
probabilityLabels = data.probabilityLabels

train = open("train.txt", encoding="utf8")
dataManager = DataManager(train)
dataManager.setCountAndProbForLabel()

test = open("test.txt", encoding="utf8")
data.setTest(test)
arrayWords = data.arrayWords
arrayLabels = data.arrayLabels
print(arrayWords)

hmm = NewHMM(dataManager.probWordForLabel,probabilityLabels)

while True:
    word = input("\n\nPut a phrase: ").split(" ")
    hmm.startSearch(word)


# from HMM import HMM
#
# print('Train data:')
# train = open("train.txt", encoding="utf8")
# databaseTrain = Data(train, 'train')

# print('\nTest data:')
# test = open("test.txt",encoding="utf8")
# hmm = HMM(train)
# # print(hmm.data[200])
# # hmm.startSearch()