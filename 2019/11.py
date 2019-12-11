from intcode import *
from Queue import *

L=[]
with open('11.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

def paint(background):
    q=Queue()
    q.put(background)
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
            q.put(p.get((x,y),background))
        if not r:break
        l,i=r
    return p

#part 1
p=paint(0)
print len(p.keys())

#part 2
p=paint(1)
K=p.keys()
X,Y=zip(*K)
for j in xrange(min(Y),max(Y)+1):
    s=''
    for i in xrange(min(X),max(X)+1):
        s+=' #'[p.get((i,j),1)]
    print s
