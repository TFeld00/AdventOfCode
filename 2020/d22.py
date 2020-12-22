import os
DAY,_,_=__file__.rpartition('.')

from alg.util import parse_with_headers

r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
d=parse_with_headers(r)

p1,p2=d['Player 1:'],d['Player 2:']

p1=list(map(int,p1))
p2=list(map(int,p2))

# Part 1
r1,r2=p1[:],p2[:]
r=1
while r1 and r2:
    a,b=r1.pop(0),r2.pop(0)
    if a>b:
        r1+=[a,b]
    else:
        r2+=[b,a]

r=r1 or r2

s=sum(i*v for i,v in enumerate(r[::-1],1))
print(s)

# Part 2
def game(p1,p2):
    d=set()
    while p1 and p2:
        state=(tuple(p1),tuple(p2))
        if state in d:
            return 1,p1
        d.add(state)
        a,b=p1.pop(0),p2.pop(0)
        if len(p1)>=a and len(p2)>=b:
            w,l=game(p1[:a],p2[:b])
            if w==1:
                p1+=[a,b]
            else:
                p2+=[b,a]
        else:
            if a>b:
                p1+=[a,b]
            else:
                p2+=[b,a]
    if p1:
        return 1,p1
    else:
        return 2,p2

w,r=game(p1[:],p2[:])

s=sum(i*v for i,v in enumerate(r[::-1],1))
print(s)