# Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional data structures?


# O(n) complexity where n is the length of the string

def hasUniqueChar(string):

	found_items = []

	for item in string:
		if item in found_items:
			return False

		found_items.append(item)

	return True

print hasUniqueChar('abcdef')
print hasUniqueChar('abcdefa')
