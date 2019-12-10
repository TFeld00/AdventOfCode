from fractions import *
from math import *
L=[]

with open('10.txt','r')as F:
    for l in F:
        L+=list(l.strip()),
d={}
for y,l in enumerate(L):
    for x,v in enumerate(l):
        if v=='.':continue
        for Y,r in enumerate(L):
            for X,V in enumerate(r):
                if V=='.':continue
                if (x,y)==(X,Y):continue
                b,a=Y-y,X-x
                g=abs(gcd(a,b))
                s=(a/g,b/g)
                d[(x,y)]=d.get((x,y),{})
                d[(x,y)][s]=d[(x,y)].get(s,[])+[(X,Y)]

MAX= max(d.keys(),key=lambda v:len(d[v]))
print MAX,
print max(map(len,d.values()))

A,B=MAX
q=[]
X=d[MAX]
X={v:sorted(X[v],key=lambda(a,b):((A-a)**2+(B-b)**2))for v in X}

s=sorted(X,key=lambda(a,b):(atan2(a,-b)+2*pi)%(2*pi))
x=1
while x:
    x=0
    for k in s:
        if X[k]:
            q+=X[k].pop(0),
            x=1
a,b= q[199]
print a*100+b
