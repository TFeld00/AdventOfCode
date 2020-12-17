import os
DAY,_,_=__file__.rpartition('.')

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

d={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        d[(i,j,0)]=c=='#'

def getN(x,y,z,d):
    s=0
    for dx in -1,0,1:
        for dy in -1,0,1:
            for dz in -1,0,1:
                if dx or dy or dz:
                    s+= d.get((x+dx,y+dy,z+dz),0)
    return s

for i in range(6):
    D={}
    # for x,y,z in {
    #         (x+dx,y+dy,z+dz)
    #         for dx in(-1,0,1)
    #         for dy in(-1,0,1)
    #         for dz in(-1,0,1)
    #         for x,y,z in d}:
    #     c=d.get((x,y,z),0)
    #     n=getN(x,y,z,d)
    #     if c==1 and 2<=n<=3:
    #         D[(x,y,z)]=1
    #     elif c==0 and n==3:
    #         D[(x,y,z)]=1

    x,y,z=zip(*d.keys())
    minX,maxX=min(x),max(x)
    minY,maxY=min(y),max(y)
    minZ,maxZ=min(z),max(z)
    for x in range(minX-1,maxX+2):
        for y in range(minY-1,maxY+2):
            for z in range(minZ-1,maxZ+2):
                c=d.get((x,y,z),0)
                n=getN(x,y,z,d)
                if c==1 and 2<=n<=3:
                    D[(x,y,z)]=1
                elif c==0 and n==3:
                    D[(x,y,z)]=1
    d=D
print (len(D))


d={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        d[(i,j,0,0)]=c=='#'

def getN(x,y,z,w,d):
    s=0
    for dx in -1,0,1:
        for dy in -1,0,1:
            for dz in -1,0,1:
                for dw in -1,0,1:
                    if dx or dy or dz or dw:
                        s+= d.get((x+dx,y+dy,z+dz,w+dw),0)
    return s

for i in range(6):
    D={}
    # for x,y,z,w in {
    #         (x+dx,y+dy,z+dz,w+dw)
    #         for dx in(-1,0,1)
    #         for dy in(-1,0,1)
    #         for dz in(-1,0,1)
    #         for dw in(-1,0,1)
    #         for x,y,z,w in d}:
    #     c=d.get((x,y,z,w),0)
    #     n=getN(x,y,z,w,d)
    #     if c==1 and 2<=n<=3:
    #         D[(x,y,z,w)]=1
    #     elif c==0 and n==3:
    #         D[(x,y,z,w)]=1

    x,y,z,w=zip(*d.keys())
    minX,maxX=min(x),max(x)
    minY,maxY=min(y),max(y)
    minZ,maxZ=min(z),max(z)
    minW,maxW=min(w),max(w)
    for x in range(minX-1,maxX+2):
        for y in range(minY-1,maxY+2):
            for z in range(minZ-1,maxZ+2):
                for w in range(minW-1,maxW+2):
                    c=d.get((x,y,z,w),0)
                    n=getN(x,y,z,w,d)
                    if c==1 and 2<=n<=3:
                        D[(x,y,z,w)]=1
                    elif c==0 and n==3:
                        D[(x,y,z,w)]=1
    d=D
print (len(D))