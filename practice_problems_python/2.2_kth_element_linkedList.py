# implement an algorithm to find the kth to last
# element of a singly linked list


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
                return current.getData()
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
            print 'test'
            next = current.getNext()
            print next.getData()
            if next.getData() == item:
                current.setNext(next.getNext())
                break
            else:
                current = current.getNext()

    def k_element(self, k):
        if k < 0:
            return "invalid k"

        pointer2 = self.head
        pointer1 = self.head

        for x in range(k - 1):
            if pointer2 is not None:
                pointer2 = pointer2.getNext()
            else:
                return "k bigger then linkedList"

        while pointer2.getNext() is not None:
            pointer2 = pointer2.getNext()
            pointer1 = pointer1.getNext()

        return pointer1.getData()


mylist = UnorderedList()

mylist.add('a')
mylist.add('b')
mylist.add('c')
mylist.add('d')
mylist.add('e')
mylist.add('f')

print mylist.k_element(6)
