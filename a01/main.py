#!/bin/python3

def binsearch(value, data):
    if len(data) == 0: return False
    if len(data) == 1: return data[0] == value
    split = len(data) // 2
    if binsearch(value, data[:split]): return True
    if binsearch(value, data[split:]): return True
    return False

def pivotsplit(pivot, data):
    lower, upper = list(), list()
    for item in data:
        if item <= pivot: lower.append(item)
        if item >= pivot: upper.append(item)
    return lower, upper


def part_1(data):
    target = 2020

    # Finding two integers that sum to 2020, one must be <= 1010
    # and the other one must be >= 1010.
    lower, upper = pivotsplit(target / 2, data)

    # Pick the shorter list as reference (linear loop) and search
    # for the sum's counterpart in the rest (log search).
    def sectsearch():
        first, remainder = sorted([lower, upper], key=lambda l: len(l))
        for item in first:
            search = 2020 - item
            if binsearch(search, remainder):
                return (item, search)
    
    res = sectsearch()

    # Print results
    print(' - Part 1: ', end='')
    if res is None:
        print('No result.')
    else:
        print(
            f'Found {res[0]} + {res[1]}; '
            f'answer is {res[0] * res[1]}.')


def part_2(data):
    target = 2020

    # Finding three elements that sum up to 2020, there must at least
    # be one among them that is <= 674.
    first, remainder = pivotsplit(target / 3, data)

    # For the other two, one must be <= half the size of the remainder
    # and the other one >= that number.
    def sectsearch():
        for idx, fi in enumerate(first):
            subtarget = target - fi
            second, third = pivotsplit(subtarget / 2, data[idx:])
            for si in second:
                search = 2020 - fi - si
                if binsearch(search, third):
                    return (fi, si, search)
        return None

    res = sectsearch()

    # Print results
    print(' - Part 2: ', end='')
    if res is None:
        print('No result.')
    else:
        print(
            f'Found {res[0]} + {res[1]} + {res[2]}; '
            f'answer is {res[0] * res[1] * res[2]}.')


if __name__ == '__main__':
    print('## Advent 01')
    with open('input/01.txt', 'r') as fh:
        # Can we take sorted data as given? :roll:
        data = sorted([int(line.strip()) for line in fh])

    part_1(data)
    part_2(data)
