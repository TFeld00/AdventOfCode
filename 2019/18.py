from heapq import *
from Queue import *
import sys

def read(F):
    m=[]
    with open(F,'r')as f:
     for l in f:
      m+=l.strip(),

    q=Queue()
    for i,l in enumerate(m):
        for j,c in enumerate(l):
            if c.isalnum() or c=='@':
                q.put((j,i,0,c,{(j,i)}))
            
    d={}
    while not q.empty():
        x,y,l,p,s=q.get()
        for dx,dy in(-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            if m[Y][X]in'#':continue
            if(X,Y)in s:continue
            
            if m[Y][X]not in '.%':
                d[p]=d.get(p,[])+[(m[Y][X],l+1)]
            else:
                q.put((X,Y,l+1,p,s|{(X,Y)}))
    return d

def ans(F,init):
    d=read(F)
    q=[(0,init,0,'')]
    r=sum(1<<(ord(v)%32) for v in d if v.islower())
    dist={}
    for c in init:
        dist[c,0]=0
    while q:
        l,N,c,p=heappop(q)
        if r==c:
            return l,p
        for i,n in enumerate(N):
            for e,L in d[n]:
                S=N[:i]+e+N[i+1:]
                C=c
                if e.islower():
                    C|=1<<(ord(e)%32)
                if e.isupper():
                    if not C&1<<(ord(e)%32):continue
                if l+L<dist.get((e,C),10**9):
                    dist[e,C]=l+L
                    heappush(q,(l+L,S,C,p+e))


l,p=ans('18.txt','@')
print l,p

l,p=ans('18_2.txt','1234')
print l,p
