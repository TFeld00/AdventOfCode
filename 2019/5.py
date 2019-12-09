from intcode import *

L=[]
with open('5.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

print'---- 1 ----'
l=dict(enumerate(L))
intcode(l,makeGen(1))

print'---- 2 ----'
l=dict(enumerate(L))
intcode(l,makeGen(5))
