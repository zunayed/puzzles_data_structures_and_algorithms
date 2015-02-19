# write code to remove duplicates from an unsorted linked list


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


def removeDupes(list):
    #build a hashtable
    if list.head is not None:
        current = list.head
        dictionary = {current.getData(): True}

        while current.getNext() is not None:
            next = current.getNext()
            if next.getData() in dictionary:
                current.setNext(next.getNext())
            else:
                dictionary[next.getData()] = True
                current = next



mylist = UnorderedList()

mylist.add(2)
mylist.add(2)
mylist.add(7)
mylist.add(7)
mylist.add(7)
mylist.add(7)

print mylist.size()

removeDupes(mylist)

print mylist.size()
