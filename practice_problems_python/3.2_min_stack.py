# implement a stack which, in addition to push and pop also has a
# function min which returns the minimum element? Push pop and min
# should all operate in O(1) time
import unittest


class StackWithMin:
    def __init__(self):
        self.items = []
        self.min_items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if len(self.min_items) == 0 or item < self.min_items[-1]:
            self.min_items.append(item)

    def pop(self):
        popped_item = self.items.pop()
        if popped_item == self.get_min():
            self.min_items.pop()
        return popped_item

    def get_min(self):
        if len(self.items) == 0:
            return None
        return self.min_items[-1]


class MinStackTests(unittest.TestCase):
 
    def test_min_val(self):
        self.stack = StackWithMin()
        self.stack.push(432)
        self.stack.push(53)
        self.stack.push(53)
        self.stack.push(99)
        self.stack.push(533)
        self.stack.push(521)
        
        self.assertEqual(53, self.stack.get_min())


if __name__ == "__main__":
    unittest.main()
