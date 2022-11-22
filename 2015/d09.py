DAY,_,_=__file__.rpartition('.')

from itertools import *

from alg.file import download_input
download_input(DAY)

d={}

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        
        a,_,b,_,c=l.split()
        c=int(c)
        d[a]=d.get(a,{})
        d[a][b]=c
        d[b]=d.get(b,{})
        d[b][a]=c

r=d.keys()
        
l=[]
for c in permutations(r):
    x=sum(d[a][b]for a,b in zip(c,c[1:]))
    l+=x,

#part 1
print(min(l))

#part 2
print(max(l))