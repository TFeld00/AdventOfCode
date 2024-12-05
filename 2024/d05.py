DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from functools import * # cmp_to_key etc..
import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=[l]
        

a,b = parse_no_headers(r)
ic=[]
r=0
for s in b:
    if all(
        (s.index(x)<s.index(y)) if x in s and y in s else 1
        for x,y in a    
    ):
        r+=s[len(s)//2]
    else:
        ic+=s,
print(r)

d={}
for x,y in a:
    d[(x,y)]=1
    d[(y,x)]=-1
r=0
for s in ic:
    s=sorted(s, key=cmp_to_key(lambda a,b:d.get((a,b),0)))
    r+=s[len(s)//2]
print(r)