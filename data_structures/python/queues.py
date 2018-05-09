import unittest


class Queue():

    """
    FIFO, first-in first-out
    """

    def __init__(self):
        self.items = []

    def enQueue(self, item):
        '''Adds a new item to the rear of the queue'''
        self.items = [item] + self.items

    def deQueue(self):
        """Removes and returns the front item from the queue"""
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def testEnQueue(self):
        self.queue.enQueue(4)
        self.assertEqual(self.queue.items, [4])

        self.queue.enQueue(3)
        self.assertEqual(self.queue.items, [3, 4])

    def testDeQueue(self):
        self.queue.enQueue(4)
        self.queue.enQueue(2)
        self.queue.enQueue(1)

        self.assertEqual(self.queue.deQueue(), 4)
        self.assertEqual(self.queue.items, [2, 1])


if __name__ == '__main__':
    unittest.main()
