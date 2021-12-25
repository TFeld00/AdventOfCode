DAY,_,_=__file__.rpartition('.')

from math import prod
from functools import cache

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

@cache
def run4(z,d,i,mx=True):
    if i==14:return z==0,[],1
    w=d
    x=(z%26)
    z//=[1, 1, 1, 1, 26, 1, 26, 26, 1, 26, 1, 26, 26, 26][i]
    if z>prod([1, 1, 1, 1, 26, 1, 26, 26, 1, 26, 1, 26, 26, 26][i+1:]):return 0,0,0
    x+=[10, 15 ,14, 15, -8, 10, -16, -4, 11, -3, 12, -7, -15, -7][i]
    if x!=w:
        z*=26
        y=(w+[2, 16, 9, 0, 1, 12, 6, 6, 3, 5, 9, 3, 2, 3][i])
        z+=y
    init=m=[0]if mx else[10**20]
    s=0
    for v in range(1,10):
        a,b,c=run4(z,v,i+1,mx)
        if a:
            if mx:
                m=max(m,[d,*b])
            else:
                m=min(m,[d,*b])
            s+=c
    return m!=init,m,s

# part 1
m=[0]
for v in range(9,0,-1):
    a,b,c=run4(0,v,0)
    if a:
        m=max(m,b)
        break
print(*m,sep='')

# part 2
m=[10**20]
for v in range(1,10):
    a,b,c=run4(0,v,0,False)
    if a:
        m=min(m,b)
        break
print(*m,sep='')
