
from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing as mp
import time
from itertools import product

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


# def findSubWords(bigWord, wordLists, subWordSize, resultList):
#     for subWord1 in wordLists[subWordSize]:
#         if bigWord.startswith(subWord1):
#             smallword = bigWord[subWordSize:]
#             for subWord2 in wordLists[6-subWordSize]:
#                 if smallword is subWord2:
#                     resultList.append("Word: " + bigWord + " : " + subWord1 + " " + subWord2)
#         elif bigWord.endswith(subWord1):
#             smallword = bigWord[:subWordSize]
#             for subWord2 in wordLists[6-subWordSize]:
#                 if smallword is subWord2:
#                     resultList.append("Word: " + bigWord + " : " + subWord1 + " " + subWord2)

# def processPartialList(listsByLengthRef, sixLetterList, results):
#     print("started process")
#     resultList = list()
#     for sixLetterWord in sixLetterList:
#         findSubWords(sixLetterWord, listsByLengthRef, 5, resultList)
#         findSubWords(sixLetterWord, listsByLengthRef, 4, resultList)

#         for threeLetterWord in listsByLengthRef[3]:
#             if sixLetterWord.endswith(threeLetterWord):
#                 smallword = sixLetterWord[:3]
#                 for otherThreeLetterWord in listsByLengthRef[3]:
#                     if smallword in otherThreeLetterWord:
#                         resultList.append("Word: " + sixLetterWord + " : " + otherThreeLetterWord + " " + threeLetterWord)
#     results.put(resultList)
#     results.close()
#     results.join_thread()
#     print("ending process")

class subWordFinder:
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

    def processWord(self,word):
        resultList = list()
        self.findSubWords(word, self.listsByLengthRef, 5, resultList)
        self.findSubWords(word, self.listsByLengthRef, 4, resultList)

        for threeLetterWord in self.listsByLengthRef[3]:
            if word.endswith(threeLetterWord):
                smallword = word[:3]
                for otherThreeLetterWord in self.listsByLengthRef[3]:
                    if smallword in otherThreeLetterWord:
                        resultList.append("Word: " + word + " : " + otherThreeLetterWord + " " + threeLetterWord)
        return resultList


start_time = time.time()
processCount = 10

words = readLines("words.txt")
listsByLength = list()
for i in range(0,7):
    listsByLength.append(getListOfLength(i, words))

results = list()
swf = subWordFinder(listsByLength)
with Pool(processes=6) as pool:
    results += pool.starmap(func=swf.processWord,
        iterable=zip(listsByLength[6]))

count=0
for result in results:
    for res in result:
        count += 1
        print(res)
print("--- count: %s" % count)
print("--- seconds: %s " % (time.time() - start_time))
# results = mp.Queue()
# sixLetterWordSections = list()
# for i in range(0,processCount):
#     sixLetterWordSections.append(list())

# i = 0
# for word in listsByLength[6]:
#     sixLetterWordSections[i%processCount].append(word)
#     i+=1

# workers = list()
# for j in range(0,processCount):
#     workers.append(Process(
#         target=processPartialList, 
#         args=(listsByLength, sixLetterWordSections[j], results,),
#         daemon=False))
#     workers[j].start()


# time.sleep(1)
# print("waiting for workers")
# print(len(workers))

# workers[0].join()
# print("one joined")
# for worker in workers:
#     worker.join()
#     print("one worker joined")

# count = 0
# while not results.empty():
#     for res in results.get():
#         print(res)
#         count += 1
# print("Count: " + str(count))