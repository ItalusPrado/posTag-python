from Data import Data

train = open("train.txt", encoding="utf8")
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
            database.addCountWord(separated[0].lower())

def setLabelCount(file):
    for text in file:
        words = text.split(' ')
        for word in words:
            separated = word.split('_')
            database.countLabelForWord(separated[0].lower(),separated[1].lower())


separateLines(train,trainTexts) # Separando arquivo
setProbWord(trainTexts) # Calculando a contagem de cada palavra (pode ser útil)
setLabelCount(trainTexts) # Calculando a contagem das labels de cada palavra
database.probabilityLabelForWord() # Calculando probabilidade para a label de cada palavra
print(database.probabilityWordsLabels["a"])
# print(database.countWordLabels['jersei'])
# print(len(database.countWordLabels))
