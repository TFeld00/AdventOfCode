DAY,_,_=__file__.rpartition('.')

from itertools import *

from alg.file import download_input
download_input(DAY)

d={}

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('.\n')
        a,_,o,n,*_,b=l.split()
        n=int(n)*[1,-1][o=='lose']
        d[a]=d.get(a,{})
        d[a][b]=n

#part 1
r=[]
for c in permutations(d.keys()):
    v=0
    for a,b in zip(c,c[1:]+c[:1]):
        v+=d[a][b]+d[b][a]
    r+=v,
print(max(r))

#part 2
r=[]
for c in permutations(d.keys()):
    v=[]
    for a,b in zip(c,c[1:]+c[:1]):
        v+=d[a][b]+d[b][a],
    for i in range(len(v)):
        r+=sum(v[:i])+sum(v[i+1:]),
print(max(r))