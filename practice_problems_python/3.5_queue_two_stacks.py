# implement a Myqueue class which implements a queue with 2 stacks


class que_made_of_stack:
    def __init__(self):
        self.items = [[], []]

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.items[0].append(item)

    def pop(self):
        if self.size() == 0:
            return None
        while len(self.items[0]) > 0:
            self.items[1].append(self.items[0].pop())

        return self.items[1].pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items[0]) + len(self.items[1])

que = que_made_of_stack()
que.push(1)
que.push(2)
que.push(3)
que.push(4)
que.push(5)

print que.pop()  # return 1
