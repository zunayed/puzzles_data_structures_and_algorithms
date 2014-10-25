import unittest

from hashtable_linked_list import UnorderedList


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

            # linked list to handle collisions
            ul = UnorderedList()
            ul.add(key, value)
            self.data[hash_value] = ul
        else:
            # slot is taken
            existing_ul = self.data[hash_value]
            existing_ul.add(key, value)

    def get(self, key):
        hash_value = self.hash_function(key, self.size)
        return self.data[hash_value].searchByKey(key).getData()


class MyTest(unittest.TestCase):

    def setUp(self):
        self.ht = HashTable()

    def testHashFunc(self):

        self.ht[45] = 'sample'
        self.assertEqual(self.ht[45], 'sample')

        self.ht[50] = 'sample2'
        self.assertEqual(self.ht[50], 'sample2')

        # collision case
        self.ht[56] = 'sample3'
        self.assertEqual(self.ht[56], 'sample3')

        # test old value
        self.assertEqual(self.ht[50], 'sample2')


if __name__ == '__main__':
    unittest.main()
