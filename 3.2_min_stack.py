# implement a stack which, in addition to push and pop also has a
# function min which returns hte minimum element? Push pop and min
# should all operate in O(1) time


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        #store value + min value as tuple
        if self.items == [] or item < self.items[-1][1]:
            #if no values in stack or if there is a new minimum
            self.items.append((item, item))
        else:
            self.items.append((item, self.items[-1][1]))

    def pop(self):
        return self.items.pop()[0]

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def getMin(self):
        if len(self.items) == 0:
            return None

        return self.items[-1][1]

stack = Stack()
stack.push(432)
stack.push(53)
stack.push(99)
stack.push(533)
stack.push(521)

print stack.getMin()

