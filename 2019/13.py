from intcode import *
from Queue import *

L=[]
with open('13.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

d={}
o=[]

BX=0;BP=0
def draw(n):
    global BX
    global BP
    o.append(n)
    if len(o)==3:
        t=o.pop()
        y=o.pop()
        x=o.pop()
        d[(x,y)]=t
        if t==4:BX=x
        if t==3:BP=x


l=dict(enumerate(L))
r=intcode(l,None,draw)
    
print d.values().count(2)


l=dict(enumerate(L))
d={}
o=[]
q=Queue()
l[0]=2
i=0
while 1:
    r=intcodeUntilRead(l,i,q.get_nowait,draw)
    if not r:break
    l,i=r
    if BX==BP:q.put(0)
    if BX<BP:q.put(-1)
    else:q.put(1)

print d[(-1,0)]

