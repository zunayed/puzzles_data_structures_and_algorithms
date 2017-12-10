#!/usr/bin/env python3
def part1():
    f = open('input/input_4.txt')
    good_pw = 0

    with f:
        for line in f:
            wl = line.strip("\n").split(" ")

            if len(wl) == len(set(w)):
                good_pw += 1

    print(good_pw)

def part2():
    f = open('input/input_4.txt')
    good_pw = 0

    with f:
        for line in f:
            wl = line.strip("\n").split(" ")
            # sort words
            wl = [''.join(sorted(w)) for w in wl]

            if len(wl) == len(set(w)):
                good_pw += 1

    print(good_pw)

def main():
    part1()
    part1()

if __name__ == "__main__":
    main()


