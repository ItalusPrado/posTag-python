from Data import Data
from DataManager import DataManager

train = open("train.txt", encoding="utf8")

dataManager = DataManager(train)
dataManager.setCountAndProbForLabel()
print(dataManager.countWordForLabel["N"])
print(dataManager.probWordForLabel["N"])








# from HMM import HMM
#
# print('Train data:')
# # train = open("train.txt", encoding="utf8")
# # databaseTrain = Data(train, 'train')
#
# print('\nTest data:')
# test = open("test.txt",encoding="utf8")
# databaseTest = Data(test, 'test')
#
# # hmm = HMM(databaseTest.getTestData())
# # print(hmm.data[200])
# # hmm.startSearch()