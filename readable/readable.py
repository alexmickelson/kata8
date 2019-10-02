# Identify all the six letter words
# that are made up of two concatenated smaller words.

# Write the program three times -
# 1) Make it as readable as you can
# 2) Optimize the program to run as fast as you can
# 3) Make it as extensible as possible

# This one runs in 40+ min

import time


def readLines(file):
    fileHandle = open(file)
    words = fileHandle.readlines()
    words = [w.rstrip() for w in words]
    return words


def hasSixLetters(word):
    return word.__len__() == 6


def contains(outer, inner):
    return inner in outer and inner != outer


def findOtherInnerWord(word, innerWord, words):
    small = word.replace(innerWord, "", 1)
    if small in words:
        return "Word: " + word + " InnerWords: " + small + " " + innerWord


if __name__ == "__main__":
    """
    Count: 88897
    Seconds: 2716.0652933120728 (about 45 min)
    4's and 2's repeated
    3's repeated
    (not checking if word starts with only if in)
    """
    start_time = time.time()
    count = 0
    words = readLines("words.txt")
    for word in words:
        if hasSixLetters(word):
            for possibleInnerWord in words:
                if contains(word, possibleInnerWord):
                    result = findOtherInnerWord(word, possibleInnerWord, words)
                    if result is not None:
                        print(result)
                        count += 1
    print('Count: ' + str(count))
    print("Seconds: %s " % (time.time() - start_time))
