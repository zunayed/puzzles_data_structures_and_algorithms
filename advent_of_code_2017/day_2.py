#!/usr/bin/env python3
import csv
from helper_func import *

def part1():
    f = get_input_file_for_day(2)
    sum = 0

    with f:
        for line in csv.reader(f, dialect="excel-tab"):
            num_line = list(map(int, line))
            num_line.sort()

            min_num = min(num_line)
            max_num = max(num_line)

            sum += max_num - min_num

        print(sum)


def get_divisable(num_line):
    # go through big num
    for x, big_num in enumerate(num_line[::-1]):
        # skip big numbers
        for small_num in num_line[:-(x+1)]:
            if big_num % small_num == 0:
                return big_num / small_num

    return 0


def part2():
    "Open and read this day's input file."
    f = get_input_file_for_day(2)
    sum = 0

    with f:
        for line in csv.reader(f, dialect="excel-tab"):
            num_line = list(map(int, line))
            num_line.sort()

            row_val = get_divisable(num_line)
            sum += row_val

        print(sum)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
