# TODO
# load word lists
# calculate optimal hash functions

import hashlib


import bitarray


def hash(input_string):
    """
    in  -> byte stream
    out -> 8 digit integer
    """
    return int(hashlib.sha1(input_string).hexdigest(), 16) % (10 ** 8)


def main():
    bit_array = (10 ** 5) * bit_array.bitarray('0')
