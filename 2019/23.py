from intcode import *
from Queue import *
from collections import defaultdict
import sys

L=[]
with open('23.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))


mem=dict(enumerate(L))
nat=None
firstNat=0
def write(i,s):
    readCheck[i]=0
    idle[i]=0
    global nat,firstNat
    outs[i]+=[s]
    if len(outs[i])==3:
        a,x,y=outs[i]
        if a==255:
            if not firstNat:print(x,y)
            firstNat=1
            nat=(x,y)
        outs[i]=[]
        queues[a].put(x)
        queues[a].put(y)
        
def read(i):
    if readCheck[i]>2:idle[i]=1
    readCheck[i]+=1
    q=queues[i]
    if q.empty():
        return -1
    return q.get_nowait()

robs=[(dict(enumerate(L)),0)for _ in xrange(50)]
queues=defaultdict(Queue)
outs=defaultdict(list)

readCheck=[0]*50
idle=[0]*50

for i in range(50):
    queues[i].put(i)

seen=[]
while 1:
    d=[1]*50
    for j in xrange(50):
        if not d[j]:continue
        l,i=robs[j]
        r=intcodeOnce(l,i,lambda:read(j),lambda s:write(j,s))
        if not r:d[j]=0
        robs[j]=r
    if sum(d)==0:break
    if sum(idle)==50 and queues[0].empty():
        if nat is not None:
            x,y=nat
            queues[0].put(x)
            queues[0].put(y)
            if y==seen:
                print nat
                break
            seen=y
            print y
            nat=None
            idle=[0]*50
            readCheck=[0]*50
