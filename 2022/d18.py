DAY,_,_=__file__.rpartition('.')

from queue import Queue

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=tuple([*map(int,l.split(','))])
        r+=[l]

s=set(r)

#part 1
area=0
for x,y,z in r:
    for dx,dy,dz in (-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1):
        X,Y,Z=x+dx,y+dy,z+dz
        area+=(X,Y,Z) not in s
print(area)

#part 2
X,Y,Z=zip(*s)
minX,maxX=min(X)-1,max(X)+1
minY,maxY=min(Y)-1,max(Y)+1
minZ,maxZ=min(Z)-1,max(Z)+1

q=Queue()
seen=set()
border=set()
area2=0
q.put((minX,minY,minZ))
while not q.empty():
    x,y,z=q.get()
    for dx,dy,dz in (-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1):
        X,Y,Z=x+dx,y+dy,z+dz
        if not (minX<=X<=maxX and minY<=Y<=maxY and minZ<=Z<=maxZ):
            continue
        pos=(X,Y,Z)
        if pos in s:
            border|={pos}
            area2+=1
        else:
            if pos in seen: continue
            q.put(pos)
            seen|={(pos)}
print(area2)
