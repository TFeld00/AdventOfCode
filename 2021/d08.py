import os
DAY,_,_=__file__.rpartition('.')

from itertools import *
COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split('|')
        l=[a.split(),b.split()]
        r+=[l]
        pass

s=0
for a,b in r:
    for d in b:
        s+=len(d) in(2,3,4,7)

print(s)

n={
    0:(0,1,2,4,5,6),
    1:(2,5),
    2:(0,2,3,4,6),
    3:(0,2,3,5,6),
    4:(1,2,3,5),
    5:(0,1,3,5,6),
    6:(0,1,3,4,5,6),
    7:(0,2,5),
    8:(0,1,2,3,4,5,6),
    9:(0,1,2,3,5,6)
}
N={*n.values()}
nR={n[d]:str(d) for d in n}
total=0
for a,b in r:
    for p in permutations('abcdefg'):
        d={tuple(sorted(map(p.index,v)))for v in a+b}
        if d<=N:
            break
    B=''.join(nR[tuple(sorted(map(p.index,v)))]for v in b)
    total+=int(B)
print(total)