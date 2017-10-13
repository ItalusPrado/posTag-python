from Data import Data
from DataManager import DataManager
from NewHMM import NewHMM

train = open("train.txt", encoding="utf8")
trainData = Data(train)
probabilityLabels = trainData.probabilityLabels

train = open("train.txt", encoding="utf8")
dataManager = DataManager(train)
dataManager.setCountAndProbForLabel()

hmm = NewHMM(dataManager.probWordForLabel,probabilityLabels)
hmm.startSearch()




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