DAY,_,_=__file__.rpartition('.')

from queue import *

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l)]
        r+=[l]
        
        
W,H=len(r[0]),len(r)


def solve(part=1):
    q=Queue()

    res=0
    x=0
    for i,l in enumerate(r):
        for j,c in enumerate(l):
            if c==0:
                x+=1
                q.put((j,i,0,x))

    s=set()
    while not q.empty():
        x,y,v,id=q.get()
        
        if v==9:
            res+=1
        
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if part==1:
                if (X,Y,id)in s:continue

            if 0<=X<W and 0<=Y<H:
                if r[Y][X]==v+1:
                    s|={(X,Y,id)}
                    q.put((X,Y,r[Y][X],id))
    print(res)

solve(1)
solve(2)