# Write code to partition a linked list around a value x, sunch
# that all nodes less than x came before all nodes greater than
# or equal to x


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

    def spitOnNumber(self, number):
        if self.head is None:
            return False

        p1 = self.head
        p2 = self.head.getNext()

        while p2 is not None:
            if p2.getData() < number:
                p1.setNext(p2.getNext())
                p2.setNext(self.head)
                p2 = p1.getNext()
            else:
                p1 = p1.getNext()
                p2 = p1.getNext()

