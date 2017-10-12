from Data import Data
from HMM import HMM

print('Train data:')
train = open("train2.txt", encoding="utf8")
databaseTrain = Data(train, 'train')

print('\nTest data:')
test = open("test2.txt",encoding="utf8")
databaseTest = Data(test, 'test')

hmm = HMM(databaseTest.getTestData())
# print(hmm.data[200])
# hmm.startSearch()