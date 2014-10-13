import unittest


class HashTable:

    """
    Hastable w/chaining
    """

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self, key):
        """
        Overriding getitem behavior to allow ht[45] type behavior
        """
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def hash_function(self, item, size):
        return item % size

    def insert(self, key, value):
        """
        Insert a key value pair into the hashtable
        """
        hash_value = self.hash_function(key, self.size)
        if self.slots[hash_value] is None:
            # Slot is open
            self.slots[hash_value] = key
            self.data[hash_value] = value

    def get(self, key):
        hash_value = self.hash_function(key, self.size)
        if self.slots[hash_value] == key:
            return self.data[hash_value]


class MyTest(unittest.TestCase):

    def setUp(self):
        self.ht = HashTable()

    def testHashFunc(self):
        self.ht[45] = 'sample'
        self.assertEqual(self.ht[45], 'sample')


if __name__ == '__main__':
    unittest.main()
