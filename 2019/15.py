from intcode import *
from Queue import *

L=[]
with open('15.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))


def draw(p):
    global X
    global Y
    K=p.keys()
    if not K:return
    x,y=zip(*K)
    for j in xrange(min(y),max(y)+1):
        s=''
        for i in xrange(min(x),max(x)+1):
            s+='D'if(X,Y)==(i,j)else '!'if(0,0)==(i,j)else p.get((i,j),' ')
        print s

X,Y=0,0
D=0
P=0
RESET=1
def move(n):
    global X,Y,D,p,d,q,P,RESET
    x,y=[(X,Y-1),(X,Y+1),(X-1,Y),(X+1,Y)][D-1]
    if n==0:
        d[(x,y)]='#'
        if not RESET:
            pd=len(p)
            P=max(P,pd)
    else:
        X,Y=x,y
        if (x,y)in d and (X,Y)==p[-2][:2]:p.pop()
        else:
            p+=[(x,y,D)]
            d[(x,y)]='.'
            for d2 in 1,2,3,4:
                i,j=[(X,Y-1),(X,Y+1),(X-1,Y),(X+1,Y)][d2-1]
                if (i,j)not in d:q+=[(x,y,d2)]
    if n==2:
        d[(x,y)]='$'
        if RESET:
            RESET=0
            print len(p)-1
            d.clear()
            d[(x,y)]='$'
            q[:]=[(x,y,i)for i in 1,2,3,4]
            p[:]=[(x,y,0)]
   
def read():
    global X,Y,D,d,q
    x,y,z=q[-1]
    if (x,y)!=(X,Y):q+=backtrack()
    x,y,z=q.pop()
    if (x,y)==(X,Y):
        D=z
        return z
    
def backtrack():
    global X,Y,D,p,d,q
    w=[]
    if not q:return[]
    a,b,_=q[-1]
    i=-1
    while (a,b)!=p[i][:2]:
        x,y,z=p[i]
        i-=1
        Z=[0,2,1,4,3][z]
        w+=[(x,y,Z)]
    return w[::-1]

l=dict(enumerate(L))
d={(0,0):'!'}
q=[(0,0,1),(0,0,2),(0,0,3),(0,0,4)]
p=[(0,0,0)]
i=0
while 1:
    r=intcodeUntilRead(l,i,read,move)
    if not r:break
    l,i=r
    if not q:break

print P-1
draw(d)
