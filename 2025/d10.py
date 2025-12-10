DAY,_,_=__file__.rpartition('.')

import re
import z3

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

## Part 1
def parse(l):
    b,*l,_ = l
    B=0
    for c in b[1:-1][::-1]:
        B*=2
        B+=c=='#'
    L=[]
    for c in l:
        x=0
        for v in [*map(int,re.findall(r'-?\d+',c))]:
            x+=1<<v
        L+=x,
    return B,L
    
def f(b,l):
    q=[[b,0]]
    s=set()
    for b,p in q:
        if b in s:continue
        s|={b}
        for w in l:
            x=b^w
            if x==0:
                return p+1
            if x not in s:
                q+=[x,p+1],

s=0
for b,l in map(parse,r):
    s+=f(b,l)

print(s)


## Part 2
def parse2(l):
    _,*l,req = [[*map(int,re.findall(r'-?\d+',c))]for c in l]
    return l,req

def f2(l,r):
    s=z3.Optimize()
    L=[]
    X=[]
    for v in r:
        L+=[[],v],
    for i,w in enumerate(l):
        x=z3.Int(f'x{i}')
        for v in w:
            L[v][0]+=x,
        s.add(x>=0)
        X+=x,
    s.minimize(sum(X))
    for a,b in L:
        s.add(sum(a)==b)
    s.check()
    m=s.model()
    return(sum (m[x].as_long() for x in X))
    
s=0
for l,r in map(parse2,r):
    s+=f2(l,r)

print(s)
