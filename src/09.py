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
    def valid(prev, curr):
        pruned = [p for p in prev if p <= curr]
        for i, v in enumerate(pruned):
            if curr - v in pruned[i:]: return True
        return False

    preamble = 25
    for values in windows(data, preamble + 1):
        prev, curr = values[:preamble], values[-1]
        if not valid(prev, curr): break

    # Print results
    print(f' - Part 1: {curr}')
    return curr


def part_2(data, target):

    def partsum():
        # Walk backwards because I'd expect less comparisons
        dlen = len(data)
        rev = data[::-1]
        for rstart in range(dlen):
            if rev[rstart] >= target: continue
            rstop = rstart + 1
            diff = target - rev[rstart]
            while diff > 0:
                diff -= rev[rstop]
                rstop += 1
            if diff == 0:
                return dlen - rstop, dlen - rstart - 1

    start, stop = partsum()
    sseq = sorted(data[start:stop + 1])
    res = sseq[0] + sseq[-1]

    # Print results
    print(f' - Part 2: {res}')


if __name__ == '__main__':
    print('## Advent 09')
    with open(INPUT, 'r') as fh:
        data = [int(line.strip()) for line in fh]

    target = part_1(data)
    part_2(data, target)
