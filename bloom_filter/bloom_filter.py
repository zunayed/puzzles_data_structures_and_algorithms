import math
import hashlib

import bitarray
import mmh3


def calc_optimal_hash_func(lenght_of_entries):
    m = (-lenght_of_entries * math.log(0.01)) / ((math.log(2)) ** 2)
    k = (m / lenght_of_entries) * math.log(2)

    return int(k)


def lookup(string, bit_array, seeds):
    for seed in range(seeds):
        result = mmh3.hash(string, seed) % len(bit_array)
        if bit_array[result] == 0:
            return "nope"

    return "Probably"


def load_words():
    data        = []
    word_loc    = '/usr/share/dict/words'

    with open(word_loc, 'r') as f:
        for word in f.readlines():
            data.append(word)

    return data


def get_bit_array():
    words       = load_words()
    w_length    = len(words)
    seeds       = calc_optimal_hash_func(w_length)
    bit_array   = w_length * bitarray.bitarray('0')

    for word in words:
        word = word.encode()
        for seed in range(seeds):
            pos = mmh3.hash(word, seed) % w_length
            bit_array[pos] = 1

    return seeds, bit_array

if __name__ == '__main__':
    seeds, ba = get_bit_array()
    print(lookup('zunayed', ba, seeds))
    print(lookup('cat', ba, seeds))
    print(lookup('hello', ba, seeds))
    print(lookup('jsalj', ba, seeds))
