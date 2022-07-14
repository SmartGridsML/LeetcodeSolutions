import unittest
from SortCharactersByFrequency import frequencySort


class MyTest(unittest.TestCase):
    def test(self):
        self.assertIn(frequencySort("tree") , {"eert" , "eetr"} )


if __name__ == '__main__':
    unittest.main()
