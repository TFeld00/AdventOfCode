DAY,_,_=__file__.rpartition('.')

from functools import cache

from alg.file import download_input
download_input(DAY)

d={}

import re

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,_,b=l.partition(' -> ')
        a=a.replace('AND','&').replace('OR','|').replace('LSHIFT','<<').replace('RSHIFT','>>').replace('NOT','~')
        a=re.sub(r'([a-z]+)',r'f("\1")',a)
        d[b]=a

#part 1
@cache
def f(c):
    if c.isdigit():
        return int(c)
    else:
        return eval(d[c])

print(v:=f('a'))

#part 2
d['b'] = str(v)
@cache
def f(c):
    if c.isdigit():
        return int(c)
    else:
        return eval(d[c])

print(f('a'))

