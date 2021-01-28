#!/usr/bin/python3

import os
import itertools
import sys


INPUT = os.path.abspath(os.path.join(__file__,
        f'../../input/{os.path.splitext(os.path.basename(__file__))[0]}.txt'))


def windows(itr, n=2):
    iters = itertools.tee(itr, n)
    for itr, num_skipped in zip(iters, itertools.count()):
        for _ in range(num_skipped):
            next(itr, None)
    return zip(*iters)


def part_1(data):
    seq = sorted([0] + data + [max(data) + 3])
    bins = {1: 0, 2: 0, 3: 0}

    for i in range(len(seq) - 1):
        diff = seq[i + 1] - seq[i]
        bins[diff] += 1

    res = bins[1] * bins[3]

    # Print results
    print(f' - Part 1: {res}')


def part_2(data):

    # Print results
    print(f' - Part 2: Not done')


if __name__ == '__main__':
    print('## Advent 10')
    with open(INPUT, 'r') as fh:
        data = [int(line.strip()) for line in fh]

    part_1(data)
    part_2(data)
