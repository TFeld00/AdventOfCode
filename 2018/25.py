r=[]

with open('25.txt','r')as f:
 for line in f:
  r+=[map(int,line.split(','))]

MAX_D=3
def dist((x,y,z,w),(X,Y,Z,W)):
 return abs(x-X)+abs(y-Y)+abs(z-Z)+abs(w-W)

R=r[:]
Q=[R.pop()]
grps=[]
g=[]
while R:
 if Q:
  current = Q.pop()
  g+=[current]
 else:
  current = R.pop()
  grps+=[g]
  g=[current]
 temp=[(p,dist(p,current)<=MAX_D)for p in R]
 neighbors = [p for p,n in temp if n]
 R=[p for p,n in temp if not n]
 Q+=neighbors

if g:grps+=[g]
print len(grps)
