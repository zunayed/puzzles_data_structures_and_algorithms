"""
Given an array nums and a value val, remove all instances of that
value in-place and return the new length.  Do not allocate extra space
for another array, you must do this by modifying the input array
in-place with O(1) extra memory.  The order of elements can be changed.
It doesn't matter what you leave beyond the new length.
"""


def remove_dupe(arr, target):
    if len(arr) < 2:
        return 1

    p1 = 0
    p2 = len(arr) - 1

    while p1 < p2:
        if arr[p1] == target:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p2 -= 1
        else:
            p1 += 1

    return p1


testcases = [
    ([3, 2, 2, 3, 2], 3),
    ([], 3),
    ([2], 3),
    ([1, 3], 3),
    ([1, 1, 3], 3),
]

for arr, target in testcases:
    ct = remove_dupe(arr, target)
    print(arr, ct)
