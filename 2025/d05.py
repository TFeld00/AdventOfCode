DAY,_,_=__file__.rpartition('.')

from itertools import pairwise
from alg.util import parse_no_headers

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l and [*map(int,l.split('-'))]
        r+=[l]

r,L=parse_no_headers(r)
r=[(x,y+1)for x,y in r]

# --

s=0
for [v] in L:
    if any (x<=v<y for x,y in r):
        s+=1
print(s)

# --

s=set()
for x,y in r:
    s|={x,y}

s2=set()
for x,y in r:
    n=set()
    for v in s:
        if x<=v<=y:
            n|={v}
    for a,b in pairwise(sorted(n)):
        s2|={(a,b)}
r=0
for a,b in s2:
    r+=b-a
print(r)