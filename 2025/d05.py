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

# --

s=0
for [v] in L:
    if any (x<=v<=y for x,y in r):
        s+=1
print(s)

# --

s=set()
for x,y in r:
    s|={x,y}

s2=set()
t=set()
for x,y in r:
    n=set()
    for v in s:
        if x<=v<=y:
            n|={v}
    for a,b in pairwise(sorted(n)):
        s2|={(a,b)}
    if len(n)==1:
        a=n.pop()
        s2|={(a,a)}
t={x for x,y in s2}
t2={x for x,y in s2 if x!=y}
r=0
for a,b in s2:
    if b in t and (a!=b or b in t2):
        b-=1
    r+=b-a+1
print(r)