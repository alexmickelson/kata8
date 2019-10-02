class WordComposition:
    def __init__(self, listsByLengthRef, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.listsByLengthRef = listsByLengthRef
    

    def findSubWords(self, bigWord, wordLists, subWordSize, resultList):
        for subWord1 in wordLists[subWordSize]:
            if bigWord.startswith(subWord1):
                smallword = bigWord[subWordSize:]
                for subWord2 in wordLists[6-subWordSize]:
                    if smallword is subWord2:
                        resultList.append("Word: " + bigWord + " : " + subWord1 + " " + subWord2)
            elif bigWord.endswith(subWord1):
                smallword = bigWord[:subWordSize]
                for subWord2 in wordLists[6-subWordSize]:
                    if smallword is subWord2:
                        resultList.append("Word: " + bigWord + " : " + subWord1 + " " + subWord2)

    def processWords(self,word):
        resultList = list()
        self.findSubWords(word, self.listsByLengthRef, 5, resultList)
        self.findSubWords(word, self.listsByLengthRef, 4, resultList)

        for threeLetterWord in self.listsByLengthRef[3]:
            if word.endswith(threeLetterWord):
                smallword = word[:3]
                for otherThreeLetterWord in self.listsByLengthRef[3]:
                    if smallword in otherThreeLetterWord:
                        resultList.append("Word: " + word + " : " + otherThreeLetterWord + " " + threeLetterWord)
        if resultList == []:
            return None
        else:
            return resultList
