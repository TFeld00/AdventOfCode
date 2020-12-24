import os
DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

def move(x,y,dir):
    if dir=='e':
        return x+1,y
    if dir=='w':
        return x-1,y
    if dir=='se':
        return x,y+1
    if dir=='sw':
        return x-1,y+1
    if dir=='ne':
        return x+1,y-1
    if dir=='nw':
        return x,y-1

d={}
for l in r:
    x,y=0,0
    for dir in re.findall(r'[ns]?[ew]',l):
        x,y=move(x,y,dir)
    v=d.get((x,y),0)
    d[(x,y)]=1-v

print(sum(d.values()))

def getN(x,y,d):
    s=0
    for dx,dy in [(1,0),(-1,0),(0,1),(-1,1),(1,-1),(0,-1)]:
            s+= d.get((x+dx,y+dy),0)
    return s

for i in range(100):
    D={}
    
    x,y=zip(*d.keys())
    minX,maxX=min(x),max(x)
    minY,maxY=min(y),max(y)
    for x in range(minX-1,maxX+2):
        for y in range(minY-1,maxY+2):
                c=d.get((x,y),0)
                n=getN(x,y,d)
                if c==1 and 1<=n<=2:
                    D[(x,y)]=1
                elif c==0 and n==2:
                    D[(x,y)]=1
    
    d=D

print(sum(d.values()))