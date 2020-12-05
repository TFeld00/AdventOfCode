import os
DAY,_,_=os.path.basename(__file__).partition('.')

from itertools import *
from collections import *
from math import *
#from fractions import *
#from queue import *
import re
import sys

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        L,R,F,B=map(ord,'LRFB')
        l=l.translate({L:'0',R:'1',F:'0',B:'1'})
        
        row,col=int(l[:7],2),int(l[7:],2)
        r+=[(row,col)]


print(max(row*8+col for row,col in r))

seats=[row*8+col for row,col in r]
a=min(seats)
b=max(seats)
print({*range(a,b+1)}-{*seats})


