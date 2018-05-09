import random
import unittest


def bubbleSort(num_list):
    pass


class MyTest(unittest.TestCase):

    def testBubbleSort(self):
        test_list = random.sample(range(10), 5)
        self.assertEqual(bubbleSort(test_list), sorted(test_list))

if __name__ == '__main__':
    unittest.main()