from intcode import *
from itertools import *

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
    lists=[[L[:],0]for _ in range(5)]
    O=[0] 
    for j,v in enumerate(p):
        O+=[v]
        l,i=lists[j]
        lists[j]=intcodeOnce(l,i,O.pop,O.append)
    j=4
    while 1:
        j=(j+1)%5
        x=lists[j]
        if not x:print j;break
        l,i=x
        r=intcodeOnce(l,i,O.pop,O.append)
        if not r and j==0:break
        lists[j]=r
    R[O[-1]]=p
print R[max(R)],
print max(R)
