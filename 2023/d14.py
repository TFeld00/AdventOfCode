DAY,_,_=__file__.rpartition('.')

import re
from alg.util import rotate90clockwise, rotate90counterclockwise

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
L=[]

m=rotate90counterclockwise(r)

for C in range(1000000000):
    for j in range(4):
        s=0
        x=[]
        for l in m:
            l=''.join(l)
            l=re.sub('[O.]+',(lambda v:''.join(sorted(v[0])[::-1])),l)
            x+=l,
        if (C,j)==(0,0): #part 1
            s=0
            for l in x:
                for i,c in enumerate(l[::-1],1):
                    if c=='O':s+=i
            print(s)
        m=rotate90clockwise(x)
    s=0
    for l in m:
        for i,c in enumerate(l[::-1],1):
            if c=='O':s+=i
        x+=l,
    
    state=''.join(map(''.join,m)),s
    if state in L:
        I=L.index(state)
        break
    L+=state,

#part 2
W=C-I
print(L[I+(1000000000-I)%W-1][1])