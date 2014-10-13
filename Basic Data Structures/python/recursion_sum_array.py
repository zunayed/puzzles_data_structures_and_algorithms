# Warm up: using no loops (for, while, etc.), and no global variables,
# write a function that returns the sum of a list:

# sum([1, 2, 3, 4, 5]) -> 15
# sum([]) -> 0


def sum(array, index):
    if index == len(array):
        return 0
    else:
        return array[index] + sum(array, index + 1)


print sum([1, 2, 3, 4, 5], 0)
