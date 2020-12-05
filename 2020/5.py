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
        
        a,b=0,127
        for c in l[:7]:
            m=(a+b)//2
            if c=='F':
                b=m
            else:
                a=m+1
        row=a
        a,b=0,7
        for c in l[7:]:
            m=(a+b)//2
            if c=='L':
                b=m
            else:
                a=m+1
        col=a
        r+=[(row,col)]


print(max(row*8+col for row,col in r))

seats=[row*8+col for row,col in r]
a=min(seats)
b=max(seats)
print({*range(a,b+1)}-{*seats})


