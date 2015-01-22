# Implement a method to perform basic string compression
# using the counts of repeated characters. For example,
# the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the
#  original string, your method should return the original string.


def compressString(string):
    new_string = ''
    for char in string:
        if char in new_string:
            pass
        else:
            new_string += char + str(string.count(char))

    return new_string


def compressString2(string):
    new_string = []
    charCount = 0
    lastChar = ''
    for char in string:
        if char == lastChar:
            charCount += 1
        else:
            if lastChar != '':
                new_string.append(lastChar + str(charCount))
            charCount = 1
        lastChar = char

    new_string.append(lastChar + str(charCount))
    return ''.join(new_string)

print compressString('aaaaabbbbcccccccccd')
print compressString2('aaaaabbbbcccccccccd')
