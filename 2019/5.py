from intcode import *

L=[]
with open('5.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

l=L[:]
intcode(l,makeGen(1))

l=L[:]
intcode(l,makeGen(5))
