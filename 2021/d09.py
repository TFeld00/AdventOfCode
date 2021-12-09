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

S={(j,i)for i in range(len(r))for j in range(len(r[i]))if r[i][j]!=9}
v=[]
while S:
    W=len(r[0])
    H=len(r)
    q=Queue()
    s=set()
    q.put(S.pop())
    size=0
    while not q.empty():
        x,y=q.get()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue
        
            if 0<=X<W and 0<=Y<H:
                if r[Y][X]!=9:
                    s|={(X,Y)}
                    q.put((X,Y))
                    size+=1
    S-=s
    v+=size,
v.sort()
print(prod(v[-3:]))