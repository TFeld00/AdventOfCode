DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=[l]

def dist(*l):
    if len(l)==2:
        (x,y),(X,Y)=l
    else:
        x,y,X,Y=l
    return abs(x-X)+abs(y-Y)
s={}
b=set()
lx=set()
for x,y,X,Y in r:
    d=dist(x,y,X,Y)
    s[x,y]=d
    b|={(X,Y)}
    
def ints(Y):
    l=[]
    for x,y in s:
        d=s[(x,y)]
        dy=abs(y-Y)
        if dy>d:continue
        lx=x-d+dy
        rx=x+d-dy
        l+=(lx,rx),
    l.sort()
    while 1:
        L=l[:1]
        for X,Y in l[1:]:
            x,y=L.pop()
            if x<=X<=y or X<=x<=Y or y+1==X or y+1==X:
                L+=(min(x,X),max(y,Y)),
            else:
                L+=(x,y),(X,Y)
        if L==l:break
        l=L
    return l


#part 1
t=0
Y=2000000
l=ints(Y)
for lx,rx in l:
   B=sum(by==Y and lx<=bx<=rx for bx,by in b)
   t+=rx-lx-B+1
print(t)

#part 2
minX=minY=0
maxX=maxY=4000000

for y in range(minY,maxY+1):
    l=ints(y)
    if len(l)>1:
        ry=y
        rx=l[0][1]+1
        t=rx*4000000+ry
        print(t)
        break