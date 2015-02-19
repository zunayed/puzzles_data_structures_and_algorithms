"""
Given 2 strings write a function that checks if s2 is a rotation of s1
"""

def is_rotation(s1, s2):
    if s1 != "" and len(s1) == len(s2):
        s1s1 = s1 + s1
        if s2 in s1s1:
            return True

    return False


s1 = "waterbottle"
s2 = "erbottlewat"

assert is_rotation(s1, s2) ==  True

s2 = "erbottlewa"

assert is_rotation(s1, s2) == False
