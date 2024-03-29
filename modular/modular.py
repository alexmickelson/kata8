import time
from typing import List, Dict, Tuple
from pprint import pprint as pp


def readLines(file: str):
    """
    Reads the file and returns an array of each row
    """
    fileHandle = open(file)
    words = fileHandle.readlines()
    words = [w.rstrip() for w in words]
    return words


def initializeMissingKeys(dictionary: Dict[int, List[str]]) -> None:
    """
    if the dictionary has keys 1, 3, 5 it will fill in the
    missing values of 0, 2, 4.
    """
    index = 0
    sortedkeys = sorted(dictionary.keys())
    lastIndex = sortedkeys[-1]
    while index < lastIndex:
        if index not in dictionary.keys():
            dictionary[index] = []
        index += 1


def sortItemsByLength(
        collection: Dict[int, List[str]]
        ) -> Dict[int, List[str]]:
    """
    places items in an array in a dictionary
    where the key is the items length
    """
    sortedCollections = {}
    for item in collection:
        if(len(item) not in sortedCollections.keys()):
            sortedCollections[len(item)] = []
        sortedCollections[len(item)].append(item)
    return sortedCollections


def wordSizesSmallerThan(word: range):
    """
    returns a range starting at 0 and going up to one less
    than the length of the word
    """
    return range(0, len(word))


def itemIsFirstPart(big: str, small: str):
    return big.startswith(small) and big != small


def itemIsLastPart(big: str, small: str):
    return big.endswith(small) and big != small


def listOfRightSizedWords(big: str,
                          small: str,
                          collections: Dict[int, List[str]]):
    return collections[len(big) - len(small)]


def getStartingWords(bigWord: str, wordCollections: Dict[int, List[str]]):
    """
    Parses the wordcollections for smaller words that are the start
    of the bigWord
    """
    sameStartingWords = []
    for index in wordSizesSmallerThan(bigWord):
        for word in wordCollections[index]:
            if itemIsFirstPart(bigWord, word):
                sameStartingWords.append(word)
    return sameStartingWords


def getCompletingWords(bigWord: str,
                       smallWord: str,
                       wordCollections: Dict[int, List[str]]):
    """
    if another word is in the collection that can append
    to smallWord to make bigWord it will return
    """
    wordToFind = bigWord[len(smallWord):]
    for secondHalf in listOfRightSizedWords(bigWord,
                                            smallWord,
                                            wordCollections):
        if wordToFind == secondHalf:
            return [wordToFind]
    return []


def findContainedWords(word: str, wordCollections: Dict[int, List[str]]
                       ) -> Tuple[str, str, str]:
    """
    finds all words wordCollections that can be combined to make word

    Returns
    --------
    an array of tuples with the structure (word, firstHalf, secondHalf)
    """
    startWords = getStartingWords(word, wordCollections)
    results = []
    for firstHalf in startWords:
        # could be more efficient if not using lists
        for secondHalf in getCompletingWords(word, firstHalf, wordCollections):
            results.append((word, firstHalf, secondHalf))
    return results


def validateTargetWordSize(size: int, collections: Dict[int, List[str]]):
    """ checks that the size of word targeted is in the collections keys"""
    if size not in collections.keys():
        raise ValueError("Target word size is not valid")


def main() -> None:
    start_time: float = time.time()
    collection: List[str] = readLines("words.txt")
    targetWordSize: int = 6

    sortedCollections: Dict[int, List[str]] = sortItemsByLength(collection)
    initializeMissingKeys(sortedCollections)

    validateTargetWordSize(size=targetWordSize, collections=sortedCollections)

    results: List[Tuple[str, str, str]] = []
    for word in sortedCollections[targetWordSize]:
        results += findContainedWords(word, sortedCollections)

    pp(results)
    print('Count: ' + str(len(results)))
    print("Seconds: %s " % (time.time() - start_time))


if __name__ == "__main__":
    """
    Count: 30599
    Seconds: 138.884605884552,

    Count: 30599
    Seconds: 147.0303237438202

    Count: 30599
    Seconds: 116.19400000572205

    Count: 30599
    Seconds: 127.60181665420532
    """
    main()
