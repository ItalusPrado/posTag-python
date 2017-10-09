class Data():

    probWords = dict()
    totalWords = 0

    def addProbWord(self,word):
        self.totalWords += 1
        if not self.probWords.__contains__(word):
            self.probWords[word] = 1
        else:
            self.probWords[word] = self.probWords[word]+1