import unittest
import optimized


class TestOptimized(unittest.TestCase):

    def test_CanGetListOfLength(self):
        dummyCollection = ['1', '22', '333', '4444', '55555', '666666']
        resCollection = optimized.getListOfLength(2, dummyCollection)
        return self.assertEqual(['22'], resCollection)

    def test_CanFindIfWordIsSubword(self):
        outerWord = 'outerWord'
        innerWord = 'Word'
        self.assertTrue(optimized.contains(outer=outerWord, inner=innerWord))

    def test_CanSortWordsByLength(self):
        dummyCollection = ['1', '22', '333', '4444', '55555', '666666']
        resultingCollection = [[], ['1'], ['22'], ['333'],
                               ['4444'], ['55555'], ['666666']]
        self.assertEqual(optimized.splitByLength(dummyCollection),
                         resultingCollection)

    def test_CanSortWordsByLengtAndFail(self):
        dummyCollection = ['1', '22', '333', '4444', '55555', '666666']
        resultingCollection = [[], [''], ['22'], ['333'],
                               ['4444'], ['55555'], ['666666']]
        self.assertNotEqual(optimized.splitByLength(dummyCollection),
                            resultingCollection)

    def test_integrationTest(self):
        dummyCollection = [[], ['1'], ['22'], ['333'],
                           ['4444'], ['55555'], ['333333', '555551']]
        results = optimized.processWords(dummyCollection, 2)
        expected = [["Word: 333333 : 333 333"], ["Word: 555551 : 55555 1"]]
        self.assertEqual(expected, results)


if __name__ == "__main__":
    unittest.main()
