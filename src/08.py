#!/usr/bin/python3

import os


INPUT = os.path.abspath(os.path.join(__file__,
        f'../../input/{os.path.splitext(os.path.basename(__file__))[0]}.txt'))


class Command:
    def __init__(self, raw):
        cmd, param = raw.split(' ')
        self.cmd = cmd
        self.param = int(param)

    def exec(self, pos, acc):
        poff, aoff = 1, 0
        if self.cmd == 'acc':
            aoff = self.param
        if self.cmd == 'jmp':
            poff = self.param
        return (poff, aoff)


def part_1(data):
    pos, acc = 0, 0
    hit = [pos]
    while True:
        poff, aoff = data[pos].exec(pos, acc)
        pos += poff
        if pos in hit: break
        hit.append(pos)
        acc += aoff

    # Print results
    print(f' - Part 1: {acc}')


def part_2(data):
    def variations():
        for p, c in enumerate(data):
            if c.cmd == 'jmp':
                replace = Command(f'nop {c.param}')
            elif c.cmd == 'nop':
                replace = Command(f'jmp {c.param}')
            yield data[:p] + [replace] + data[p+1:]

    def play(variant):
        pos, acc = 0, 0
        hit = [pos]
        while True:
            if pos == len(variant): return acc
            poff, aoff = variant[pos].exec(pos, acc)
            pos += poff
            if pos in hit: raise
            hit.append(pos)
            acc += aoff

    res = None
    for cmds in variations():
        try: res = play(cmds)
        except: continue

    # Print results
    print(f' - Part 2: {res}')


if __name__ == '__main__':
    print('## Advent 08')
    with open(INPUT, 'r') as fh:
        data = [Command(line.strip()) for line in fh]

    part_1(data)
    part_2(data)
