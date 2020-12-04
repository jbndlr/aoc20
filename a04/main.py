#!/usr/bin/python3

import re

RE_YEAR = re.compile(r'^\d{4}$')
RE_HEIGHT = re.compile(r'^\d{2,3}((in)|(cm))$')
RE_HCOLOR = re.compile(r'^#[0-9a-f]{6}$')
RE_ECOLOR = re.compile(r'^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$')
RE_PID = re.compile(r'^\d{9}$')
RE_ANY = re.compile(r'^.*$')


class Passport:
    fields = {
        'byr': RE_YEAR, 'iyr': RE_YEAR, 'eyr': RE_YEAR, 'hgt': RE_HEIGHT,
        'hcl': RE_HCOLOR,'ecl': RE_ECOLOR, 'pid': RE_PID, 'cid': RE_ANY
    }

    def __init__(self, raw):
        self.data = {field: None for field in Passport.fields.keys()}
        for field in raw.split(' '):
            key, value = field.strip().split(':')
            self.data[key] = value

    def __str__(self):
        return ' '.join([f'{k}:{v}' for k, v in self.data.items()])

    def valid_1(self, exceptions=[]):
        missing = (
            set(Passport.fields.keys())
            - {k for k, v in self.data.items() if v is not None}
            - set(exceptions))
        return len(missing) == 0

    def valid_2(self, exceptions=[]):
        missing = (
            set(Passport.fields.keys())
            - {k for k, v in self.data.items() if v is not None}
            - set(exceptions))
        if len(missing) > 0:
            return False

        for key, value in self.data.items():
            if key == 'cid': continue
            if not Passport.fields[key].match(value): return False
            if key == 'byr' and (int(value) < 1920 or int(value) > 2002): return False
            if key == 'iyr' and (int(value) < 2010 or int(value) > 2020): return False
            if key == 'eyr' and (int(value) < 2020 or int(value) > 2030): return False
            if key == 'hgt':
                if value[-2:] == 'cm':
                    if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        return False
                elif value[-2:] == 'in':
                    if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        return False
                else:
                    return False
        return True


def part_1(data):
    res = sum([
        1
        for passport in data
        if passport.valid_1(exceptions=['cid'])])

    # Print results
    print(f' - Part 1: {res}')


def part_2(data):
    res = sum([
        1
        for passport in data
        if passport.valid_2(exceptions=['cid'])])

    # Print results
    print(f' - Part 2: {res}')


if __name__ == '__main__':
    print('## Advent 04')

    data = []
    with open('input/01.txt', 'r') as fh:
        buf = []
        for line in fh:
            if line[0] == '\n':
                data.append(Passport(' '.join(buf)))
                buf = []
            else:
                buf.append(line)
        if len(buf):
            data.append(Passport(' '.join(buf)))

    part_1(data)
    part_2(data)
