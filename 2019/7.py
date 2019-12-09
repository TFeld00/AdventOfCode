from intcode import *
from itertools import *
from Queue import *
from heapq import *

L=[]
with open('7.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

print '--- PART 1 ---'
R={}
for p in permutations(range(5)):
    O=[0]
    for v in p:
        O+=[v]
        l=L[:]
        intcode(l,O.pop,O.append)
    R[O[0]]=p
print R[max(R)],
print max(R)

print '--- PART 2 ---'
R={}
for p in permutations(range(5,10)):
    I=[Queue()for _ in range(5)]
    lists=[[L[:],0]for _ in range(5)]
    io=[[I[i].get_nowait,I[(i+1)%5].put]for i in range(5)]
    O=[0]
    for j,v in enumerate(p):
        I[j].put(v)
        
    I[0].put(0)
    j=4
    while 1:
        j=(j+1)%5
        x=lists[j]
        l,i=x
        r=intcodeUntilRead(l,i,*io[j])
        if not r and j==4:break
        lists[j]=r
    R[I[0].get_nowait()]=p
print R[max(R)],
print max(R)
