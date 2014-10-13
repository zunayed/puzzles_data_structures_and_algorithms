import unittest


class Stack:

    """
    LIFO, last-in first-out
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Adds a new item to the top of the stack. It needs the item and returns nothing
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the top item from the stack. It needs no parameters and returns the item
        """
        return self.items.pop()

    def peek(self):
        """
        Returns the top item from the stack but does not remove it. It needs no parameters
        """
        return self.items[-1]   # Alternately self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class MyTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def testPushStack(self):
        self.stack.push(4)
        self.stack.push(3)
        self.stack.push(2)

        self.assertEqual(self.stack.items, [4, 3, 2])

    def testPopStack(self):
        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)


if __name__ == '__main__':
    unittest.main()
