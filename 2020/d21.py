import os
DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l,_,b=l.partition('(contains ')
        b=b[:-1]
        l=l.split()
        b=b.split(', ')
        r+=[(l,b)]

i=set()
d={}
for l,b in r:
    for c in b:
        s=d.get(c,set(l))
        s&=set(l)
        d[c]=s
    i|=set(l)
s=set(i)
for v in d:
    s-=d[v]

S=0
for v in s:
    for l,b in r:
        S+=l.count(v)
print(S)

for v in d:
    x=d[v]
    if len(x)==1:
        for w in d:
            if v!=w:
                d[w]-=x

d2={d[v].pop():v for v in d}
print(','.join(sorted(d2,key=d2.get)))