import os
DAY,_,_=__file__.rpartition('.')

from itertools import *
from collections import *
from math import *
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, whitespace, punctuation, printable
from alg.dijkstra import dijkstra
from img.img import read_img, write_img     #write_img(DAY,COLS)
from alg.util import parse_with_headers, parse_skip_headers, parse_no_headers
from functools import *
from fractions import *
from textwrap import wrap
from datetime import *
from queue import *
import heapq
from functools import cache
import sympy    #sympy.primefactors
import re
import sys

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        #l=map(int,l.split())
        #l=l.split()
        #l=int(l)
        #l=list(l)
        #print(l)
        r+=[l]
        pass
#W,H=len(r[0]),len(r)
#d=parse_with_headers(r)

a,b=[*map(int,r)]


v=20201227
print((7**8)%v)
print((7**11)%v)
print((7**3)%v)


#a,b=5764801,17807724
x=7
i=1
while x!=a:
    i+=1
    x=(x*7)%v
x=7
j=1
while x!=b:
    j+=1
    x=(x*7)%v

print(i,j)

x=a
for _ in range(j-1):
    x=(x*a)%v
print(x)
x=b
for _ in range(i-1):
    x=(x*b)%v

print(x)