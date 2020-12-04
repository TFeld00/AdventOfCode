import os
DAY, _, _ = os.path.basename(__file__).partition('.')

import re
import sys

r = []
s = 0

p = {}

with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l = l.rstrip('\n')
        if l:
            for v in l.split():
                a, b = v.split(':')
                p[a] = b
        else:
            r += p,
            p = {}

if p: r += p,

for p in r:
    if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= set(p.keys()):
        s += 1
print(s)

s2 = 0


def val(p):
    v = p.get('byr', '')
    if not (v.isdigit() and 1920 <= int(v) <= 2020): return 1
    v = p.get('iyr', '')
    if not (v.isdigit() and 2010 <= int(v) <= 2020): return 2
    v = p.get('eyr', '')
    if not (v.isdigit() and 2020 <= int(v) <= 2030): return 3
    v = p.get('hgt', '')
    v, u = v[:-2], v[-2:]
    if u == 'cm':
        if not (v.isdigit() and 150 <= int(v) <= 193): return 4
    elif u == 'in':
        if not (v.isdigit() and 59 <= int(v) <= 76): return 5
    else: return 6
    v = p.get('hcl', '')
    if not (re.match(r'^#[0-9a-f]{6}$', v)): return 7
    v = p.get('ecl', '')
    if not v in 'amb blu brn gry grn hzl oth'.split(): return 8
    v = p.get('pid', '')
    if not (v.isdigit() and len(v) == 9): return 9

    return 0


for p in r:
    #print(p)
    if not val(p):
        s2 += 1
    #else:print(val(p))
print(s2)