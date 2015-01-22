# add 2 numbers represented by linked list
# each node containing 1 digit and the ones digit
# is the head of the linked list


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


def addLists(l1, l2):
    p1 = l1.head
    p2 = l2.head
    newList = UnorderedList()
    carry = 0
    while (p1 is not None) or (p2 is not None) or (carry is not 0):
        sum = carry
        if p1 is not None:
            sum += p1.getData()
            p1 = p1.getNext()
        if p2 is not None:
            sum += p2.getData()
            p2 = p2.getNext()
        newList.add(sum % 10)
        carry = sum / 10
    return newList

mylist = UnorderedList()
mylist2 = UnorderedList()

mylist.add(7)
mylist.add(8)
mylist.add(9)

mylist2.add(4)
mylist2.add(5)
mylist2.add(6)

a = addLists(mylist, mylist2)

b = a.head

print b.getData(), b.getNext().getData(), b.getNext().getNext().getData(), b.getNext().getNext().getNext().getData()
