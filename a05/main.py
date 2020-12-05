#!/usr/bin/python3

class Boardingpass:
    def __init__(self, raw):
        self.seat = int(
            raw.replace('B', '1').replace('F', '0')
               .replace('R', '1').replace('L', '0'),
            base=2)
        self.row = self.seat >> 3
        self.col = self.seat & 7

    def __str__(self):
        return f'r: {self.row}, c: {self.col}, s: {self.seat}'


def part_1(data):
    maxseat = max([Boardingpass(line).seat for line in data])

    # Print results
    print(f' - Part 1: {maxseat}')


def part_2(data):
    seats = sorted([Boardingpass(line).seat for line in data])
    seat = None
    for idx in range(1, len(seats)):
        if seats[idx - 1] == seats[idx] - 2:
            seat = seats[idx] - 1
            break

    # Print results
    print(f' - Part 2: {seat}')


if __name__ == '__main__':
    print('## Advent 05')
    with open('input/01.txt', 'r') as fh:
        data = [line.strip() for line in fh]

    part_1(data)
    part_2(data)
