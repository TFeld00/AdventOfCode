DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from collections import Counter
from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        pass

s,r=parse_no_headers(r)
s=s[0]

d={}
for l in r:
    a,b=l.split(' -> ')
    d[a]=b

D={}
for a,b in zip(s,s[1:]):
    c=a+b
    D[c]=D.get(c,0)+1
    
C=Counter(s)

for t in range(40):
    D2={}
    for v in D:
        if v in d:
            a,b=v
            c=d[v]
            D2[a+c]=D2.get(a+c,0)+D[v]
            D2[c+b]=D2.get(c+b,0)+D[v]
            C[c]+=D[v]
    D=D2
    if t in (9,39):
        a,*_,b=C.most_common()
        print(a[1]-b[1])