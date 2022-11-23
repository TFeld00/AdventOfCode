DAY,_,_=__file__.rpartition('.')

from queue import *

from alg.file import download_input
download_input(DAY)

n=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        n=int(l)


def wall(x,y):
    s=x*x + 3*x + 2*x*y + y + y*y + n
    return bin(s).count('1')%2


def bfs(x,y,tX,tY):
    q=Queue()
    s=set()
    q.put((x,y,0))
    d=0
    while not q.empty():
        x,y,l=q.get()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue

            if (X,Y)==(tX,tY):
                #WIN
                return l+1
            
            s|={(X,Y)}
            if 0<=X and 0<=Y:
                if not wall(X,Y):
                    q.put((X,Y,l+1))

    
#part 1
print(bfs(1,1,31,39))


#part 2
q=Queue()
s=set()
q.put((1,1,0))
d=0
while not q.empty():
    x,y,l=q.get()
    if l>50:break
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        X,Y=x+dx,y+dy
        if (X,Y)in s:continue
        
        s|={(X,Y)}
        if 0<=X and 0<=Y:
            if not wall(X,Y):
                q.put((X,Y,l+1))
                d+=1
print(d)