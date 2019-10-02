import unittest
import unittest.mock as mock
import optimized

class TestOptimized(unittest.TestCase):

    def test_CanGetListOfLength(self):
        dummyCollection = ['1', '22', '333', '4444', '55555', '666666']
        resCollection = optimized.getListOfLength(2, dummyCollection)
        return self.assertEqual(['22'], resCollection)
    
    def test_CanFindIfWordIsSubword(self):
        outerWord = 'outerWord'
        innerWord = 'Word'
        self.assertTrue(optimized.contains(outer=outerWord,inner=innerWord))


    def test_CanSortWordsByLength(self):
        dummyCollection = ['1', '22', '333', '4444', '55555', '666666']
        resultingCollection = [ [], ['1'], ['22'], ['333'], ['4444'], ['55555'], ['666666']]
        self.assertEqual(optimized.splitByLength(dummyCollection), resultingCollection)

    def test_CanSortWordsByLengtAndFail(self):
        dummyCollection = ['1', '22', '333', '4444', '55555', '666666']
        resultingCollection = [ [], [''], ['22'], ['333'], ['4444'], ['55555'], ['666666']]
        self.assertNotEqual(optimized.splitByLength(dummyCollection), resultingCollection)

    @mock.patch('optimized.Pool')
    def test_FindsCorrectCompositeWords(self, mock_pool):
        dummyListsByLength = [ [], [''], ['22'], ['333'], ['4444'], ['55555'], ['444422']]
        expected = ["a correct result"]
        returnValue = mock_pool.return_value
        returnValue.starmap = mock.MagicMock(returnValue=expected)
        returnValue.return_value = expected
        
        self.assertEqual(expected, optimized.processWords(dummyListsByLength, processCount=1))


if __name__ == "__main__":
    unittest.main()