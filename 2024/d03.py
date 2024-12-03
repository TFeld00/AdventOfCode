DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l
        
# Part 1

def mul(a,b):
    return a*b

s=0
for v in re.findall('mul\(-?\d+,-?\d+\)',t):
    s+=eval(v)
print(s)

# Part 2
d=1
def mul(a,b):
    return a*b if d else 0

s=0
for v in re.findall('mul\(-?\d+,-?\d+\)|do\(\)|don\'t\(\)',t):
    if v=="don't()":
        d=0
    elif v=='do()':
        d=1
    else:
        s+=eval(v)
print(s)