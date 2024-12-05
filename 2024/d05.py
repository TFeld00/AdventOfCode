DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
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
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if d.get((s[i],s[j]),0)<0:
                s[i],s[j]=s[j],s[i]
    r+=s[len(s)//2]
print(r)