# TODO
# load word lists
# calculate optimal hash functions
import sys
import re
import hashlib

import bitarray


def fnv32a( str ):
    hval = 0x811c9dc5
    fnv_32_prime = 0x01000193
    uint32_max = 2 ** 32
    for s in str:
        hval = hval ^ ord(s)
        hval = (hval * fnv_32_prime) % uint32_max
    return hvalm


def sha1(input_string):
    """
    in  -> byte stream
    out -> 8 digit integer
    """
    return int(hashlib.sha1(input_string).hexdigest(), 16) % (20)


def load_words():
    word_loc = '/usr/share/dict/words'
    data = []
    with open(word_loc, 'r') as f:
        for word in f.readlines():
            data.append(word)

    return data


def main():
    bit_array = (20) * bitarray.bitarray('0')
    words = load_words()

    import pdb;pdb.set_trace()

if __name__ == '__main__':
    main()
