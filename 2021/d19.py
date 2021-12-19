DAY,_,_=__file__.rpartition('.')

from collections import *
from alg.util import parse_with_headers, parse_skip_headers, parse_no_headers, get_neigbors_both, get_neigbors_diag, get_neigbors_orto
from functools import cache

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        if ',' in l:
            l=[*map(int,l.split(','))]
        r+=[l]
        pass

r=parse_with_headers(r)
S=[*r.values()]

def rotations(m):
    R=set()
    mx=m
    for _ in range(4):
        mx=rot90x(mx)
        my=mx
        for _ in range(4):
            my=rot90y(my)
            mz=my
            for _ in range(4):
                mz=rot90z(mz)
                R|={mz}
    return R

def rot90x(m):
    return tuple((x,-z,y)for x,y,z in m)
def rot90y(m):
    return tuple((-z,y,x)for x,y,z in m)
def rot90z(m):
    return tuple((-y,x,z)for x,y,z in m)

pos={0:(0,0,0)}
B={0:tuple(map(tuple,S[0]))}

@cache
def has_overlap(a,b):
    s1=B[a]
    for s2 in rotations(S[b]):
        offsets=[(X-x,Y-y,Z-z)for x,y,z in s1 for X,Y,Z in s2]
        c=Counter(offsets)
        (x,y,z),v=c.most_common(1)[0]
        if v>=12:
            return True,x,y,z,move(s2,x,y,z)
    return False,0,0,[]

def move(s,x,y,z):
    return [(X-x,Y-y,Z-z)for X,Y,Z in s]

Q=[*range(1,len(S))]
def check():
    for a in B:
        for b in Q:
            v=has_overlap(a,b)
            if v[0]:
                return b,v

while Q:
    b,v=check()
    Q.remove(b)
    _,x,y,z,s=v
    B[b]=s
    pos[b]=(x,y,z)

#part 1
beacons=set()
for s in B:
    beacons|={*B[s]}

print(len(beacons))

#part 2
def d(a,b):
    x,y,z=a
    X,Y,Z=b
    return abs(X-x)+abs(Y-y)+abs(Z-z)
p=pos.values()
print(max(d(a,b)for a in p for b in p))