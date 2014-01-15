# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end
# of the string to hold the additional characters, and that you
# are given the "true" length of the string.


def replaceWhiteSpace(string):
    temp = []
    for item in string:
        if item == ' ':
            item = '%20'
        #Avoid using the + and += operators to accumulate a string
        #within a loop. Since strings are immutable, this creates
        #unnecessary temporary objects and results in quadratic rather
        #than linear running time. Instead, add each substring to a list
        #and ''.join the list after the loop terminates
        #(or, write each substring to a cStringIO.StringIO buffer).
        temp.append(item)

    return ''.join(temp)


#using list comprehension
def replaceWhiteSpace2(string):
    return ''.join(['%20' if item == ' ' else item for item in string])


print replaceWhiteSpace('What it do ?')
print replaceWhiteSpace2('What it do ?')

