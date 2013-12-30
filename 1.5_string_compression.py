# Implement a method to perform basic string compression 
# using the counts of repeated characters. For example, 
# the string aabcccccaaa would become a2blc5a3. If the 
# "compressed" string would not become smaller than the
#  original string, your method should return the original string.

def compressString(string):
	new_string = ''
	for item in string:
		if item in new_string:
			pass
		else:
			new_string += item + str(string.count(item))

	return new_string

print compressString('aaaaabbbbccccccccc')

