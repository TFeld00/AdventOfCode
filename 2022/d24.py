DAY,_,_=__file__.rpartition('.')

from queue import *

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
W,H=len(r[0]),len(r)


state=[set(),set(),set(),set(),set()]
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='.':y=0
        elif c=='<':y=1
        elif c=='>':y=2
        elif c=='^':y=3
        elif c=='v':y=4
        else:continue
        state[y]|={(j,i)}

steps={0:state}

def step(state):
    f,l,r,u,d=state
    all=f|l|r|u|d
    L={(x-1 if x>1 else W-2,y)for x,y in l}
    R={(x+1 if x<W-2 else 1,y)for x,y in r}
    U={(x,y-1 if y>1 else H-2)for x,y in u}
    D={(x,y+1 if y<H-2 else 1)for x,y in d}
    F=all-L-R-U-D
    return F,L,R,U,D

p1=False

q=Queue()
seen=set()
q.put((1,0,0,1,0,0))
while not q.empty():
    x,y,l,t,s,g=q.get()
    
    if (x,y)==(1,0) and g:
        s=1
    if (x,y)==(W-2,H-1):
        if s and g:
            print(l) #part 2
            #WIN
            break
        else:
            if not p1:
                print(l) #part 1
                p1=True
            g=1

    if t not in steps:
        steps[t]=step(steps[t-1])
    free,*_=steps[t]

    for dx,dy in (0,1),(0,-1),(1,0),(-1,0),(0,0):
        X,Y=x+dx,y+dy
        if (X,Y,t,s,g)in seen:continue

        seen|={(X,Y,t,s,g)}

        if 0<=X<W and 0<=Y<H:
            if (X,Y)in free:
                q.put((X,Y,l+1,t+1,s,g))
