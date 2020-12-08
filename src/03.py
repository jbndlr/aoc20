#!/usr/bin/python3

import os
from functools import reduce


INPUT = os.path.abspath(os.path.join(__file__,
        f'../../input/{os.path.splitext(os.path.basename(__file__))[0]}.txt'))


def part_1(data):
    idx = 0
    hit = 0
    llen = len(data[0])
    for line in data:
        if line[idx] == '#': hit += 1
        idx = (idx + 3) % llen

    # Print results
    print(f' - Part 1: {hit}')


def part_2(data):

    pattern = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = []

    llen = len(data[0])
    for p in pattern:
        idx = 0
        hit = 0
        for line in data[::p[1]]:
            if line[idx] == '#': hit += 1
            idx = (idx + p[0]) % llen
        results.append(hit)

    res = reduce((lambda x, y: x * y), results)

    # Print results
    print(f' - Part 2: {res}')


if __name__ == '__main__':
    print('## Advent 03')
    with open(INPUT, 'r') as fh:
        data = [line.strip() for line in fh]

    part_1(data)
    part_2(data)
