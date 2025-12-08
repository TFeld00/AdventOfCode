DAY,_,_=__file__.rpartition('.')

from itertools import combinations
from collections import Counter
_pow = pow
from math import *
pow = _pow

from alg.file import download_input
download_input(DAY)

r=[]
s=0
t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=[l]
        
        
H=len(r)
p={i:i for i in range(H)}
s={i:1 for i in range(H)}

# find
def f(n):
    if p[n]!=n:
        p[n]=f(p[n])
    return p[n]

# union
def g(a,b):
    x,y=f(a),f(b)
    if x!=y:
        if s[x]>s[y]:
            x,y=y,x
        p[x]=y
        s[y]+=s[x]
        return 1

D=[]

for i,j in combinations(range(H),2):
    a,b=r[i],r[j]
    d=dist(a,b)
    D+=(d,i,j),

D.sort()

R=0

for n,(d,i,j) in enumerate(D):
    a=g(i,j)
    if n==1000: # part 1
        D1=Counter()
        for i in range(H):
            x=f(i)
            D1[x]=s[x]

        print(prod(v for _,v in D1.most_common(3)))

    if a: #part 2
        a,b=r[i],r[j]
        R=a[0]*b[0]
print(R)