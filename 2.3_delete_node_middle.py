# implement an algorithm to delete a node in the middle of
# a singly listed list, given only access to the node


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

# copy over values from next node into middle node and delete the next node


def removeMiddleNode(node):
    if node.getNext() is None:
        return False
    else:
        next = node.getNext()
        node.setData(next.getData())
        node.setNext(next.getNext())
        return True


mylist = UnorderedList()

mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.add(6)
print mylist.size()

middleNode = mylist.search(4)
removeMiddleNode(middleNode)

print mylist.size()
print mylist.search(4)
