from heapq import *

depth=9465
target= 13,704

#depth=510
#target=10,10

X,Y=target
m={}
def ty(x,y):
 if (x,y)in m:return m[(x,y)]
 if x==y==0 or (x,y)==target:e=0
 elif x==0:e=16807*y
 elif y==0:e=48271*x
 else:
  e1,t1=ty(x-1,y)
  e2,t2=ty(x,y-1)
  e=e1*e2
 e=(e+depth)%20183
 t=e%3
 m[(x,y)]=(e,t)
 return m[(x,y)]

# 0 torch
# 1 climb
# 2 nothing
start=(0,0,0)
goal=(0,X,Y)

visited={}
q=[]
heappush(q,(0,start,[(0,start)]))
while q:
 v,n,path=heappop(q)
 T,X,Y=n
 if n in visited:continue
 visited[n]=v
 if n==goal:
  print v
  break
 else:
  e=ty(X,Y)[1]
  if e==0:t=1 if T==0 else 0
  if e==1:t=1 if T==2 else 2
  if e==2:t=2 if T==0 else 0
  c=(t,X,Y)
  if c not in visited:
   heappush(q,(v+7,c,path+[(1,c)]))
  for x,y in(0,1),(0,-1),(-1,0),(1,0):
   c=(T,X+x,Y+y)
   if c[1]<0 or c[2]<0:continue
   if c[2]>1000 or c[1]>50:continue
   e=ty(c[1],c[2])[1]
   if (T==0 and e in(0,2))\
   or (T==1 and e in(0,1))\
   or (T==2 and e in(1,2)):
    heappush(q,(v+1,c,path+[(0,c)]))

print v,n,len(path)
sw=sum(a for a,b in path)
print sw*7+(len(path)-sw)-1
