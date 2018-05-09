#Write a function revstring(mystr) that uses a stack
#to reverse the characters in a string.
import unittest


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def revstring(mystr):
    string = Stack()
    for item in mystr:
        string.push(item)

    reverse = ''
    
    while not string.isEmpty():
        reverse += string.pop()

    return reverse


class MyTest(unittest.TestCase):
    def testWords(self):
        self.assertEqual(revstring('apple'), 'elppa')
        self.assertEqual(revstring('x'), 'x')
        self.assertEqual(revstring('zunayed'), 'deyanuz')

    def testNumbers(self):
        self.assertEqual(revstring('718'), '817')
        self.assertEqual(revstring('1234567890'), '0987654321')


if __name__ == '__main__':
    unittest.main()
