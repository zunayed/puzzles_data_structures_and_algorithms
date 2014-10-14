import unittest


class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.getNext()

        return count

    def search(self, item):
        found = False
        current = self.head
        while current is not None and not found:
            if current.getData() == item:
                return current
            current = current.getNext()

        return found

    # def remove(self, item):
    #     current = self.head
    #     previous = None
    #     found = False
    #     while not found:
    #         if current.getData() == item:
    #             found = True
    #         else:
    #             previous = current
    #             current = current.getNext()

    #     if previous is None:
    #         self.head = current.getNext()
    #     else:
    #         previous.setNext(current.getNext())

    def remove(self, item):
        current = self.head
        if current.getData() == item:
            self.head = self.head.getNext()

        while current.getNext() is not None:
            next = current.getNext()
            if next.getData() == item:
                current.setNext(next.getNext())
                break
            else:
                current = current.getNext()


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.my_list = UnorderedList()
        self.my_list.add(31)
        self.my_list.add(77)
        self.my_list.add(17)
        self.my_list.add(93)
        self.my_list.add(26)
        self.my_list.add(54)

    def testSearch(self):
        self.assertEqual(self.my_list.search(31).getData(), 31)

    def testSizeList(self):
        self.assertEqual(self.my_list.size(), 6)

    def testEmptyList(self):
        new_list = UnorderedList()
        self.assertEqual(new_list.size(), 0)

    def testRemoveElemFromList(self):
        self.my_list.remove(31)
        self.assertEqual(self.my_list.size(), 5)


if __name__ == '__main__':
    unittest.main()
