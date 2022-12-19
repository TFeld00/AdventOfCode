DAY,_,_=__file__.rpartition('.')

import re
from alg.file import download_input
download_input(DAY)

r=[]
n=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=[l]

def h(state):
    (rO,rC,rOb,rG),(o,c,ob,g),(tO,tC,tOb,tG)=state
    return tG*10000+tOb*100+tC*10+tO

def f(steps,B):
    q=[((1,0,0,0),(0,0,0,0),(0,0,0,0))]

    for t in range(steps,0,-1):
        next=set()
        for (rO,rC,rOb,rG),(o,c,ob,g),(tO,tC,tOb,tG) in q:
            nO,nC,nOb,nG=rO,rC,rOb,rG

            total = (tO+nO,tC+nC,tOb+nOb,tG+nG)
            mO=max(B[0],B[1],B[2],B[4])
            if o>=B[4] and ob>= B[5]:
                next|={((rO,rC,rOb,rG+1),(o+nO-B[4],c+nC,ob+nOb-B[5],g+nG),total)}

            if t>1 and rOb<B[5] and o>=B[2] and c>= B[3]:
                next|={((rO,rC,rOb+1,rG),(o+nO-B[2],c+nC-B[3],ob+nOb,g+nG),total)}

            if t>1 and rC<B[3] and o>=B[1]:
                next|={((rO,rC+1,rOb,rG),(o+nO-B[1],c+nC,ob+nOb,g+nG),total)}

            if t>1 and rO<mO and o>=B[0]:
                next|={((rO+1,rC,rOb,rG),(o+nO-B[0],c+nC,ob+nOb,g+nG),total)}

            next|={((rO,rC,rOb,rG),(o+nO,c+nC,ob+nOb,g+nG),total)}
        q = sorted(next,key=h,reverse=True)[:1000]
    return max(q,key=h)[2][3]

#part 1
s=0
for i,*l in r:
    l=tuple(l)
    g=f(24,l)
    s+=i*g
    print(i,g,sep=':',end=' ')
print()
print(s)

# #part 2
p=1
for i,*l in r[:3]:
    l=tuple(l)
    g=f(32,l)
    p*=g
    print(i,g,sep=':',end=' ')
print()
print(p)