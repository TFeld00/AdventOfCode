from collections import *
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
            
    #s=set()
    d={}
    #q.put((X,Y,0,[('@',0)]))
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

d=read('18.txt')
q=[]
s=set()
r=sum(1<<(ord(v)%32) for v in d if v.islower())
heappush(q,(0,'@',0,''))
dist = defaultdict(lambda: float('inf'))
dist['@', 0] = 0
while q:
    l,n,c,p=heappop(q)
    #print l,n,c
    if r==c:
        print l,p;break
    for e,L in d[n]:
        C=c
        if e.islower():
            C|=1<<(ord(e)%32)
        if e.isupper():
            if not C&1<<(ord(e)%32):continue
        if l+L<dist[e,C]:
            dist[e,C]=l+L
            heappush(q,(l+L,e,C,p+e))
        s|={(e,c)}


d=read('18.2.txt')
q=[(0,'1234',0,'')]
r=sum(1<<(ord(v)%32) for v in d if v.islower())
dist = defaultdict(lambda: float('inf'))
dist['1234', 0] = dist['1234', 0] = dist['1234', 0] = dist['1234', 0] = 0
while q:
    l,N,c,p=heappop(q)
    #print l,n,c
    if r==c:
        print l,p;break
    for i,n in enumerate(N):
        for e,L in d[n]:
            S=N[:i]+e+N[i+1:]
            C=c
            if e.islower():
                C|=1<<(ord(e)%32)
            if e.isupper():
                if not C&1<<(ord(e)%32):continue
            if l+L<dist[e,C]:
                dist[e,C]=l+L
                heappush(q,(l+L,S,C,p+e))
                
