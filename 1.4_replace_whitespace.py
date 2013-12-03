# Write a method to replace all spaces in a string with '%20'.
# Youmay assume that the string has sufficient space at the end 
# of the string to hold the additional characters, and that you 
# are given the "true" length of the string. 

#one way
def replaceWhiteSpace(string):
	new_string = ''
	for item in string:
		if item == ' ':
			item = '%20'

		new_string += item

	return new_string

#using list comprehension 
def replaceWhiteSpace2(string):
	return ''.join(['%20' if item == ' ' else item for item in string])


print replaceWhiteSpace('What it do ?')
print replaceWhiteSpace2('What it do ?')

