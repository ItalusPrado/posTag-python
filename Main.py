from Data import Data

train = open("train.txt")
database = Data()

trainTexts = [] # Array com cada texto

def separateLines(file,array):
    content = file.readlines()
    for line in range(0, len(content)):
        array.append(content[line])

def setProbWord(file):
    for text in file:
        words = text.split(' ')
        for word in words:
            separated = word.split('_')
            database.addProbWord(separated[0].lower())



separateLines(train,trainTexts)
setProbWord(trainTexts)
print(database.probWords)
