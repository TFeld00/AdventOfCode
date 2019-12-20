from intcode import *
from Queue import *
import sys

L=[]
with open('19.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

b=0
m={}
def write(s):
    global b,m,X,Y
    b+=s
    m[X,Y]=s

q=sum([[X,Y]for X in range(50)for Y in range(50)],[])
q=q[::-1]
def read():
    global q
    return q.pop()


b=0
for x in range(50):
    for y in range(50):
        l=dict(enumerate(L))
        i=0
        q=[y,x]
        X,Y=x,y
        intcode(l,q.pop,write)
print b

w49=min(x for x in range(50)if m[x,49])
W49=max(x for x in range(50)if m[x,49])

m={}
R=[]
def write(s):
    global m,X,Y
    m[X,Y]=s

x,y=0,49
w,W=w49,W49
while 1:
    x=w
    while 1:
        l=dict(enumerate(L))
        q=[y,x]
        X,Y=x,y
        intcode(l,q.pop,write)
        if m.get((x,y),0):break
        x+=1
    w=x
    x=W
    while 1:
        l=dict(enumerate(L))
        q=[y,x]
        X,Y=x,y
        intcode(l,q.pop,write)
        if not m.get((x,y),0):break
        x+=1
    W=x-1
    y+=1
    R+=[(w,W)]
    if len(R)>99:
        w1,W1=R[-100]
        if W1-w>98:
            print w*10000+y-100
            break
