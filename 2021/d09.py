DAY,_,_=__file__.rpartition('.')

_pow = pow
from math import *
pow = _pow
from queue import *

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=map(int,l)
        l=list(l)
        r+=[l]
        pass

s=0
for i,l in enumerate(r):
    for j,c in enumerate(l):
        n=[l[j-1]]*(j>0)+l[j+1:j+2]+[r[i-1][j]]*(i>0)
        if i<len(r)-1:n+=r[i+1][j],
        if c<min(n):s+=1+c
print(s)

from alg.floodfill import fill

s=[l[:]for l in r]
S={(j,i)for i in range(len(s))for j in range(len(s[i]))if s[i][j]!=9}
A=[]
while S:
    x,y = S.pop()
    c,a = fill(s,(x,y),'',lambda c,n:n!=9)
    S-=a
    A+=c,
A.sort()
print(prod(A[-3:]))
