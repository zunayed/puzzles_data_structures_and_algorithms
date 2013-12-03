#Given two strings, write a method to decide if one is a permutation of 
#the other

def compareString(string1, string2):
	#if len of strings don't match no need to do any other checking
	if len(string1) != len(string2):
		return False

	#sort the strings and compare letter by letter
	if sorted(string1) == sorted(string2):
		return True

print compareString('abcd','dcba')
print compareString('abcd','dcbaa')
