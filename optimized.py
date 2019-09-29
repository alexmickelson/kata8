
import threading
import time

def readLines(file):
    fileHandle = open(file)
    words = fileHandle.readlines()
    words = [w.strip() for w in words]
    return words
def getListOfLength(len, words):
    newlist = list()
    for w in words:
        if w.__len__() is len:
            newlist.append(w)
    return newlist
def contains(outer, inner):
    return inner in outer


class Worker(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                listsByLengthRef=None, sixLetterList=None, resultList=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,daemon=daemon)
        self.listsByLengthRef = listsByLengthRef
        self.sixLetterList = sixLetterList
        self.resultList = resultList
    
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

    def run(self):
        for sixLetterWord in self.sixLetterList:
            self.findSubWords(sixLetterWord, self.listsByLengthRef, 5, self.resultList)
            self.findSubWords(sixLetterWord, self.listsByLengthRef, 4, self.resultList)

            for threeLetterWord in self.listsByLengthRef[3]:
                if sixLetterWord.endswith(threeLetterWord):
                    smallword = sixLetterWord[:3]
                    for otherThreeLetterWord in self.listsByLengthRef[3]:
                        if smallword in otherThreeLetterWord:
                            self.resultList.append("Word: " + sixLetterWord + " : " + otherThreeLetterWord + " " + threeLetterWord)




start_time = time.time()
threadcount = 2

words = readLines("words.txt")
listsByLength = list()
for i in range(0,7):
    listsByLength.append(getListOfLength(i, words))


results = list()
sixLetterWordSections = list()
for i in range(0,threadcount):
    sixLetterWordSections.append(list())
    results.append(list())

i = 0
for word in listsByLength[6]:
    sixLetterWordSections[i%threadcount].append(word)
    i+=1

workers = list()
for j in range(0,threadcount):
    workers.append(Worker(listsByLengthRef=listsByLength, sixLetterList=sixLetterWordSections[j], resultList=results[j]))
    workers[j].start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

finalResults = list()
count = 0
for res in results:
    finalResults+=res
    count += len(res)

for result in finalResults:
    print(result)
print(str(count) + " results")
print("--- %s seconds ---" % (time.time() - start_time))