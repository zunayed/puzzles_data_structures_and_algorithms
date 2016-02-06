# TODO
# Need 7 hash functions for an optimal bloom filter
# get more hash functions ? use a combination of 2 hash functions
import re
import sys
import math
import hashlib

import bitarray
import mmh3

def fnv32a(input_string):
    input_string = input_string.decode('utf-8')
    hval = 0x811c9dc5
    fnv_32_prime = 0x01000193
    uint32_max = 2 ** 32
    for s in input_string:
        hval = hval ^ ord(s)
        hval = (hval * fnv_32_prime) % uint32_max

    return hval


def sha1(input_string):
    """
    in  -> byte stream
    out -> 8 digit integer
    """
    return int(hashlib.sha1(input_string).hexdigest(), 16)


def calc_optimal_hash_func(lenght_of_entries):
    m = (-lenght_of_entries * math.log(0.01)) / ((math.log(2)) ** 2)
    k = (m / lenght_of_entries) * math.log(2)

    return k


def lookup(string, bit_array, seeds):
    for seed in xrange(seeds):
        result = abs(mmh3.hash(string, seed)) % len(size)
        if bit_array[result] == 0:
            return "Nope"

    return "Probably"


def load_words():
    word_loc = '/usr/share/dict/words'
    data = []
    with open(word_loc, 'r') as f:
        for word in f.readlines():
            data.append(word)

    return data


def main():
    words       = load_words()
    w_length    = len(words)
    seeds       = calc_optimal_hash_func(w_length)
    bit_array   = w_length * bitarray.bitarray('0')

    for word in words:
        word = word.encode()
        for seed in range(seeds):
            pos = abs(mmh3.hash(word, seed)) % w_length
            bit_array[pos] = 1


if __name__ == '__main__':
    main()
