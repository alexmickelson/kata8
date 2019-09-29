# Identify all the six letter words 
# that are made up of two concatenated smaller words.

# Write the program three times - 
    # 1) Make it as readable as you can
    # 2) Optimize the program to run as fast as you can
    # 3) Make it as extensible as possible
def readLines(file):
    fileHandle = open(file)
    words = fileHandle.readlines()
    words = [w.rstrip() for w in words]
    return words
def hasSixLetters(word):
    return word.__len__() == 6
def contains(outer, inner):
    return outer.endswith(inner) and (inner is not outer)
def findOtherInnerWord(word, innerWord, words):
    small = word.replace(innerWord,"",1)
    if small in words:
        return "Word: " + word + " InnerWords: " + small + " " + innerWord


words = readLines("words.txt")
for word in words:
    if hasSixLetters(word):
        for possibleInnerWord in words:
            if contains(word, possibleInnerWord):
                result = findOtherInnerWord(word, possibleInnerWord, words)
                if result is not None:
                    print(result)
