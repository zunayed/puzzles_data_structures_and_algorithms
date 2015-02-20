# Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional data structures?

def has_unique_char(string):
    """
    O(n) complexity where n is the length of the string
    """

    found_items = []

    for item in string:
        if item in found_items:
            return False

        found_items.append(item)

    return True

print has_unique_char('abcdef')
print has_unique_char('abcdefa')
