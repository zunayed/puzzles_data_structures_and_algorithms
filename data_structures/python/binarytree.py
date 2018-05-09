import unittest


class BinaryTree:

    def __init__(self, root):
        """
        Set root of tree
        """
        self.tree = [root, [], []]

    def insert(self, direction, root, new_branch):
        """
        Insert a new branch
        """
        if direction.lower() == 'left':
            popped_branch = root.pop(1)
            if len(popped_branch) > 1:
                root.insert(1, [new_branch, popped_branch, []])
            else:
                root.insert(1, [new_branch, [], []])

            return root
        elif direction.lower() == 'right':
            popped_branch = root.pop(2)
            if len(popped_branch) > 1:
                root.insert(2, [new_branch, [], popped_branch])
            else:
                root.insert(2, [new_branch, [], []])

            return root

    def get_root(self, root):
        return root[0]

    def set_root_val(self, root, new_val):
        root[0] = new_val


def get_child(direction, root):
    if direction.lower() == 'left':
        return root[1]
    elif direction.lower() == 'right':
        return root[2]
    else:
        return "provide proper direction"


class MyTest(unittest.TestCase):

    def test_initial(self):
        bt = BinaryTree(3)
        self.assertEqual(bt.tree, [3, [], []])

        bt.set_root_val(bt.tree, 9)
        self.assertEqual(bt.tree, [9, [], []])

    def test_insert(self):
        bt = BinaryTree(3)
        bt.insert("left", bt.tree, 4)
        self.assertEqual(bt.tree, [3, [4, [], []], []])

        bt.insert("left", bt.tree, 5)
        self.assertEqual(bt.tree, [3, [5, [4, [], []], []], []])

        bt.insert("right", bt.tree, 6)
        self.assertEqual(bt.tree, [3, [5, [4, [], []], []], [6, [], []]])

        bt.insert("right", bt.tree, 7)
        self.assertEqual(bt.tree, [3, [5, [4, [], []], []], [7, [], [6, [], []]]])


if __name__ == '__main__':
    unittest.main()
