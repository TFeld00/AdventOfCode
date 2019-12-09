from intcode import *
from itertools import *
from Queue import *
from heapq import *

L=[]
with open('9.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

#part 1
l=dict(enumerate(L))
intcode(l,makeGen(1))


#part 2
l={}
l=dict(enumerate(L))
intcode(l,makeGen(2))
