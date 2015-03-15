class SetOfStacks(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, val):
        # Case where there are no stacks or stack is full
        if (len(self.stacks) == 0) or (len(self.stacks[-1]) == self.capacity):
            self.stacks.append([])

        self.stacks[-1].append(val)

    def pop(self):
        if self.stacks:
            val = self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0:
                del self.stacks[-1]

            return val
        else:
            return None

def test_stack():
    setofstacks = SetOfStacks(4)
    for x in range(16):
        setofstacks.push(x)
        print "pushing", x

    for i in range(5):
        print "Poping", setofstacks.pop()

    print setofstacks.stacks

if __name__ == "__main__":
    test_stack()
