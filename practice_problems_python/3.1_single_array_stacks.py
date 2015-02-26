# implement 3 stacks with a single array
import unittest


class SingleArrayStacks(object):

    def __init__(self, array_size=100, number=3):
        self.array = [None] * array_size
        self.pointer = [-1, -1, -1]
        self.stack_size = array_size // number

    def get_top_position(self, stack_number):
        return stack_number * self.stack_size + self.pointer[stack_number]

    def push(self, stack_number, val):
        if self.pointer[stack_number] < self.stack_size - 1:
            self.array[self.get_top_position(stack_number) + 1] = val
            self.pointer[stack_number] += 1

        else:
            return "Stack full"

    def pop(self, stack_number):
        if self.pointer[stack_number] == -1:
            return 'Stack is empty'

        pop_val = self.array[self.get_top_position(stack_number)]
        self.array[self.get_top_position(stack_number)] = None
        self.pointer[stack_number] -= 1

        return pop_val


class StackTests(unittest.TestCase):

    def test_push_pop(self):
        self.array = SingleArrayStacks()
        self.assertEqual('Stack is empty', self.array.pop(0))

        self.array.push(0, 1)
        self.array.push(0, 2)
        self.array.push(0, 3)

        self.assertEqual(3, self.array.pop(0))
        self.assertEqual(2, self.array.pop(0))
        self.assertEqual(1, self.array.pop(0))

        self.array.push(1, 1)
        self.array.push(2, 1)
        self.array.push(2, 2)
        self.array.push(2, 3)

        self.assertEqual(3, self.array.pop(2))
        self.assertEqual(2, self.array.pop(2))
        self.assertEqual(1, self.array.pop(2))
        self.assertEqual(1, self.array.pop(1))

    def test_stack_full(self):
        self.array = SingleArrayStacks(array_size=9)
        self.array.push(2, 1)
        self.array.push(2, 2)
        self.array.push(2, 3)

        self.assertEqual('Stack full', self.array.push(2, 4))


if __name__ == "__main__":
    unittest.main()
