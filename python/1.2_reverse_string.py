#Implement a function void revers(char*str) in C or C++ which reverses a
#null terminated string


def reverse(string):
    if string is not "":
        return string[-1:] + reverse(string[:-1])
    else:
        return ""

print reverse('zunayed')
