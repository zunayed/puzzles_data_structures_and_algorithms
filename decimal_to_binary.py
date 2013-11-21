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
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def printByTwo(num):
    bin = Stack()
    while num > 0:
        bin.push(num % 26)
        num = num // 26
        
    binString = ""
    while not bin.isEmpty():
        binString = binString + str(bin.pop())

    return binString


print printByTwo(26)

   
