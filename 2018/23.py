import z3
bots=[]
with open('23.txt','r')as f:
 for line in f:
  l=line[:-1]
  p,r=l.split(', ')
  P=map(int,p[5:-1].split(','))
  R=int(r[2:])
  bots+=[(P,R)]

def dist((x,y,z),(X,Y,Z)):
 return abs(X-x)+abs(Y-y)+abs(Z-z)

# Part 1
mB,mR=max(bots,key=lambda (p,r):r)
c=0
for b,_ in bots:
 if dist(b,mB)<=mR:
  c+=1
print 'Part 1:',c
#

# Part 2
x,y,z=zip(*zip(*bots)[0])
minX,maxX=min(x),max(x)
minY,maxY=min(y),max(y)
minZ,maxZ=min(z),max(z)

print minX,maxX
print minY,maxY
print minZ,maxZ

print(maxX-minX)*(maxY-minY)*(maxZ-minZ)
