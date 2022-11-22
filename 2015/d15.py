DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b,c,d,e = map(int,re.findall(r'-?\d+',l))
        r+=[(a,b,c,d,e)]

R=[]
for i in range(101):
    li=[v*i for v in r[0]]
    for j in range(101-i):
        lj=[li[x]+v*j for x,v in enumerate(r[1])]
        for k in range(101-i-j):
            lk=[lj[x]+v*k for x,v in enumerate(r[2])]
            for l in range(101-i-j-k):
                a,b,c,d,e=[max(0,lk[x]+v*l) for x,v in enumerate(r[3])]
                v=a*b*c*d
                R+=[v,e],

#part 1
print(max(R)[0])

#part 2
print(max(v for v,e in R if e==500))