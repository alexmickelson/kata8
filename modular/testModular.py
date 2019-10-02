import unittest
import modular

class testModular(unittest.TestCase):

    def test_GetRightRangeForIndexes(self):
        expected = range(0,2)
        actual = modular.wordSizesSmallerThan("aa")
        self.assertEqual(expected,actual)


    def test_GetRightRangeForIndexes(self):
        expected = range(0,3)
        actual = modular.wordSizesSmallerThan("a4a")
        self.assertEqual(expected,actual)


    def test_canGetStartingWords(self):
        dummyCollection = {
            0: [],
            1: ['a'],
            2: ['ab'],
            3: ['ade'],
            4: ['abcd']
            }
        expected = ['a', 'ab']
        acutal = modular.getStartingWords('abcd', dummyCollection)
        self.assertEqual(expected, acutal)


    def test_GetsCorrectCompletingWords(self):
        dummyCollection = {
            0: [],
            1: ['a'],
            2: ['ab'],
            3: ['ade'],
            4: ['abcd']
            }
        expected = ['a']
        actual = modular.getCompletingWords('endswitha', 'endswith', dummyCollection)
        self.assertEqual(expected, actual)


    def test_CompletingWordsHandlesIfNotFound(self):
        dummyCollection = {
            0: [],
            1: [],
            2: ['ab'],
            3: ['ade'],
            4: ['abcd']
            }
        expected = []
        actual = modular.getCompletingWords('endswitha', 'endswith', dummyCollection)
        self.assertEqual(expected, actual)

    def test_GetCorrespondingWords(self):
        bigword = 'thanos'
        smallword='than'
        dummyCollection = {
            0: [],
            1: ['a'],
            2: ['ab', 'os'],
            3: ['ade'],
            4: ['abcd']
            }
        expected = ['os']
        actual = modular.getCompletingWords(bigword, smallword, dummyCollection)
        self.assertEqual(expected, actual)
    
    def test_findWordPartsFromCollections(self):
        dummyCollection = {
            0: [],
            1: ['a'],
            2: ['ab', 'os'],
            3: ['ade'],
            4: ['abcd', 'than'],
            5: ['asdff']
            }
        compositeWord='thanos'
        expected = [('thanos', 'than', 'os')]
        actual = modular.findContainedWords(compositeWord, dummyCollection)
        self.assertEqual(expected, actual)
    

    def test_findContainedWordsHandlesIfNoSecondHalf(self):
        dummyCollection = {
            0: [],
            1: ['a'],
            2: ['ab', 'os'],
            3: ['ade'],
            4: ['abcd', 'than', 'chad'],
            5: ['asdff']
            }
        wordToFind = 'chadius'
        expected = []
        #actual = modular.findContainedWords(wordToFind, dummyCollection)
        #self.assertEqual(expected, actual)

    def test_sortsItemsCorrectly(self):
        dummyArray=['a', 'aa', 'aaa']
        expected = {
            1: ['a'], 
            2: ['aa'], 
            3: ['aaa']
            }
        actual = modular.sortItemsByLength(dummyArray)
        self.assertEqual(expected, actual)

    def test_initializeMissingKeys(self):
        startDictionary = {3: []}
        expected = {
            0: [],
            1: [],
            2: [],
            3: []
        }
        modular.initializeMissingKeys(startDictionary)
        self.assertEqual(expected, startDictionary)


    def test_validateTargetWordSize(self):
        with self.assertRaises(ValueError):
            modular.validateTargetWordSize(9, {0:[]})
        

if __name__ == "__main__":
    unittest.main()
    