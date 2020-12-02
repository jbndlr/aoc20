#!/bin/python3

class PasswordEntry:
    def __init__(self, raw):
        policy, char, entry = raw.split(' ')
        pmin, pmax = policy.split('-')
        self.pmin = int(pmin)
        self.pmax = int(pmax)
        self.char = char[0]
        self.entry = entry

    def valid_1(self):
        count = sum([1 for c in self.entry if c == self.char])
        return self.pmin <= count <= self.pmax

    def valid_2(self):
        first = self.entry[self.pmin - 1] == self.char
        second = self.entry[self.pmax - 1] == self.char
        return first != second


def part_1(data):
    count = sum([1 for e in data if e.valid_1()])

    # Print results
    print(f' - Part 1: {count}')


def part_2(data):
    count = sum([1 for e in data if e.valid_2()])

    # Print results
    print(f' - Part 2: {count}')


if __name__ == '__main__':
    print('## Advent 02')
    with open('input/01.txt', 'r') as fh:
        data = [PasswordEntry(line.strip()) for line in fh]

    part_1(data)
    part_2(data)
