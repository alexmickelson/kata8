
import multiprocessing
from multiprocessing import Pool
import time
from composition import WordComposition


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


def splitByLength(allWords):
    listsByLength = list()
    for i in range(0,7):
        listsByLength.append(getListOfLength(i, allWords))
    return listsByLength


def processWords(listsByLength, processCount):
    results = list()
    wordCompositionFinder = WordComposition(listsByLength)
    with Pool(processes=processCount) as pool:
        results += pool.starmap(func=wordCompositionFinder.processWords,
            iterable=zip(listsByLength[6]))
    return results


def getCountAndPrint(items):
    itemCount=0
    for item in items:
        itemCount += 1
        print(item)


if __name__ == "__main__":
    processCount = 5
    start_time = time.time()

    listsByLength = splitByLength(readLines("words.txt"))
    #process words by set unions as well
    results = processWords(listsByLength, processCount)

    resultCount = getCountAndPrint(results)
    print("--- count: %s" % resultCount)
    print("--- seconds: %s " % (time.time() - start_time))