#!/usr/bin/python3

from functools import reduce


class Group:
    def __init__(self, raw):
        self.anyone = reduce(
            (lambda a, b: a | b),
            [{char for char in line.strip()} for line in raw])
        self.everyone = reduce(
            (lambda a, b: a & b),
            [{char for char in line.strip()} for line in raw])


def part_1(data):
    count = sum([len(Group(group).anyone) for group in data])

    # Print results
    print(f' - Part 1: {count}')


def part_2(data):
    count = sum([len(Group(group).everyone) for group in data])

    # Print results
    print(f' - Part 2: {count}')


if __name__ == '__main__':
    print('## Advent 06')

    data = []
    with open('input/01.txt', 'r') as fh:
        buf = []
        for line in fh:
            if line[0] == '\n':
                data.append(buf)
                buf = []
            else:
                buf.append(line)
        if len(buf):
            data.append(buf)

    part_1(data)
    part_2(data)
