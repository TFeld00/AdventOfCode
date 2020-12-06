import os
DAY,_,_=__file__.rpartition('.')

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
        l=l.translate(str.maketrans('FBLR','0101'))
        
        row,col=int(l[:7],2),int(l[7:],2)
        r+=[(row,col)]


print(max(row*8+col for row,col in r))

seats=[row*8+col for row,col in r]
a=min(seats)
b=max(seats)
print({*range(a,b+1)}-{*seats})


