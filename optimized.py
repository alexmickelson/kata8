
import threading

def readLines(file):
    fileHandle = open(file)
    words = fileHandle.readlines()
    words = [w.rstrip() for w in words]
    return words
def getListOfLength(len, words):
    newlist = list()
    for w in words:
        if w.__len__() is len:
            newlist.append(w)
    return newlist
def contains(outer, inner):
    return inner in outer

words = readLines("words.txt")

listsByLength = list()
listsByLength.append(getListOfLength(0, words))
listsByLength.append(getListOfLength(1, words))
listsByLength.append(getListOfLength(2, words))
listsByLength.append(getListOfLength(3, words))
listsByLength.append(getListOfLength(4, words))
listsByLength.append(getListOfLength(5, words))
listsByLength.append(getListOfLength(6, words))

for sixLetterWord in listsByLength.__getitem__(6):

    for fiveLetterWord in listsByLength.__getitem__(5):
        if sixLetterWord.startswith(fiveLetterWord):
            smallword = sixLetterWord[5:]
            for oneLetterWord in listsByLength.__getitem__(1):
                if smallword is oneLetterWord:
                    print("Word: " + sixLetterWord + " :  " + fiveLetterWord + " " + oneLetterWord)
        elif sixLetterWord.endswith(fiveLetterWord):
            smallword = sixLetterWord[:5]
            for oneLetterWord in listsByLength.__getitem__(1):
                if smallword is oneLetterWord:
                    print("Word: " + sixLetterWord + " :  " + fiveLetterWord + " " + oneLetterWord)
    for fourLetterWords in listsByLength.__getitem__(4):
        if sixLetterWord.endswith(fiveLetterWord):
            smallword = sixLetterWord[:5]
            for oneLetterWord in listsByLength.__getitem__(1):
                if smallword is oneLetterWord:
                    print("Word: " + sixLetterWord + " :  " + fiveLetterWord + " " + oneLetterWord)