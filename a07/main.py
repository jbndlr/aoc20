#!/usr/bin/python3

class Bag:
    def __init__(self, raw):
        this, others = raw.split('contain')
        self.color = ' '.join(this.split(' ')[:2])
        self.outer = set()
        self.inner = dict()
        for kind in others.replace('.', '').split(', '):
            parts = kind.split('bag')[0].strip().split(' ')
            if parts[0] != 'no':
                self.inner[' '.join(parts[1:])] = int(parts[0])

    def __str__(self):
        return (
            f'{self.color}: '
            + ', '.join([
                f'{v} {k}'
                for k, v in self.inner.items()]))

    def __hash__(self):
        return hash(self.color)


def part_1(lookup):
    for bag in lookup.values():
        for icolor, ibag in bag.inner.items():
            try:
                lookup[icolor].outer.add(bag)
            except KeyError:
                continue # if an outmost bag is hit

    possible = set()
    def unwrap(bag):
        if not len(bag.outer): return
        for outer in bag.outer:
            possible.add(outer)
            unwrap(outer)
    unwrap(lookup['shiny gold'])

    # Print results
    print(f' - Part 1: {len(possible)}')


def part_2(lookup):
    def wrap(bag):
        if not len(bag.inner): return 1
        return 1 + sum([
            count * wrap(lookup[color])
            for color, count in bag.inner.items()])

    count = wrap(lookup['shiny gold']) - 1

    # Print results
    print(f' - Part 2: {count}')


if __name__ == '__main__':
    print('## Advent 05')
    with open('input/01.txt', 'r') as fh:
        data = [Bag(line.strip()) for line in fh]

    lookup = {}
    for bag in data:
        if bag.color not in lookup.keys():
            lookup[bag.color] = bag

    part_1(lookup)
    part_2(lookup)
