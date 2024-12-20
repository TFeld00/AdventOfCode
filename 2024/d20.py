DAY,_,_=__file__.rpartition('.')

from queue import *

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='S':
            xs,ys=j,i
        elif c=='E':
            xe,ye=j,i


def bfs(r,xs,ys,xe,ye,d):
    W=len(r[0])
    H=len(r)
    q=Queue()
    s={(xs,ys)}
    q.put((xs,ys,0))
    while not q.empty():
        x,y,l=q.get()
        d[(x,y)]=l
        
        if (x,y)==(xe,ye):
            return l
        
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue

            s|={(X,Y)}
            if 0<=X<W and 0<=Y<H:
                if r[Y][X]!='#':
                    q.put((X,Y,l+1))


ds={}
score = bfs(r,xs,ys,xe,ye,ds)
de={}
_ = bfs(r,xe,ye,xs,ys,de)

res1=0
res2=0

for (x,y),ss in ds.items():
    for (X,Y),se in de.items():
        dx,dy=abs(X-x),abs(Y-y)
        s=ss+se+dx+dy
        if s<=score-100:
            if dx+dy<=2:
                res1+=1
            if dx+dy<=20:
                res2+=1
print(res1)
print(res2)
