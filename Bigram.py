class Bigram():
    word = ""
    wordLabel = ""
    previousWord = ""
    # dicionario = {"verbo" : {"verbo":5,"substantivo": 10}, "subs": {"verbo":5,"substantivo": 10}}
    probability = 0.0

    def __init__(self, word, wordLabel, previousWord, probability):
        self.word = word
        self.wordLabel = wordLabel
        self.previousWord = previousWord
        self.probability = probability

    def __getProbability__(self):
        return self.probability

