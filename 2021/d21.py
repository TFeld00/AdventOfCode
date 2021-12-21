DAY,_,_=__file__.rpartition('.')

from itertools import cycle, product
from collections import Counter
from functools import cache

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        l=int(l[-1])
        r+=[l]

d=cycle(range(1,101))
R=r[:]

#part 1
s=[0,0]
p=0
x=0
while max(s)<1000:
    roll=next(d)+next(d)+next(d)
    x+=3
    r[p]=(r[p]+roll)%10 or 10
    s[p]+=r[p]
    p=1-p
print(min(s)*x)

#part 2
r=R[:]
s=[0,0]
p=0

C=Counter(map(sum,product((1,2,3),repeat=3)))

@cache
def turn(s1,s2,p,p1,p2):
    if s1>=21:
        return 1,0
    elif s2>=21:
        return 0,1
    
    pos=(p1,p2)[p]
    resa,resb=0,0
    for roll in C:
        pos1=(pos+roll)%10 or 10
        if p:
            a,b = turn(s1,s2+pos1,1-p,p1,pos1)
        else:
            a,b = turn(s1+pos1,s2,1-p,pos1,p2)
        resa+=C[roll]*a
        resb+=C[roll]*b
    return resa,resb

result = turn(0,0,p,*r)
print(max(result))