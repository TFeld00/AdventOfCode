from intcode import *
from Queue import *

L=[]
with open('11.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))


q=Queue()
q.put(0)
p={}
x,y,d=0,0,0
l=dict(enumerate(L))
i=0
while 1:
    o=[]
    r=intcodeUntilRead(l,i,q.get_nowait,o.append)
    if o:
        p[(x,y)]=o.pop(0)
    if o:
        dd=1 if o.pop(0)else-1
        d=(d+dd)%4
        x,y=[(x,y-1),(x+1,y),(x,y+1),(x-1,y)][d]
        q.put(p.get((x,y),0))
    if not r:break
    l,i=r
K=p.keys()
print len(K)

q=Queue()
q.put(1)
p={}
x,y,d=0,0,0
l=dict(enumerate(L))
i=0
while 1:
    o=[]
    r=intcodeUntilRead(l,i,q.get_nowait,o.append)
    if o:
        p[(x,y)]=o.pop(0)
    if o:
        dd=1 if o.pop(0)else-1
        d=(d+dd)%4
        x,y=[(x,y-1),(x+1,y),(x,y+1),(x-1,y)][d]
        q.put(p.get((x,y),1))
    if not r:break
    l,i=r
K=p.keys()
X,Y=zip(*K)
for j in xrange(min(Y),max(Y)+1):
    s=''
    for i in xrange(min(X),max(X)+1):
        s+=' #'[p.get((i,j),1)]
    print s
