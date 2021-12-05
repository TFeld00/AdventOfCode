import os
DAY,_,_=__file__.rpartition('.')

from itertools import *
from collections import *
_pow = pow
from math import *
pow = _pow
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

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        #l=map(int,l.split())
        a,_,b=l.split()
        #l=int(l)
        #l=list(l)
        x,y=map(int,a.split(','))
        X,Y=map(int,b.split(','))
        #print(l)
        r+=[((x,y),(X,Y))]
        pass
#W,H=len(r[0]),len(r)


a=[[0]*1000 for _ in range(1000)]
for (x,y),(X,Y)in r:
    if x==X or y==Y:
        x,X=sorted((x,X))
        y,Y=sorted((y,Y))
        for i in range(x,X+1):
            for j in range(y,Y+1):
                a[i][j]+=1

print(sum(v>1 for l in a for v in l ))



a=[[0]*1000 for _ in range(1000)]
for (x,y),(X,Y)in r:
    if x==X:
        y,Y=sorted((y,Y))
        for j in range(y,Y+1):
            a[x][j]+=1
    elif y==Y:
        x,X=sorted((x,X))
        for j in range(x,X+1):
            a[j][y]+=1
    else:
        (x,y),(X,Y)=sorted([(x,y),(X,Y)])
        d=1 if y<Y else -1
        for i in range(x,X+1):
            a[i][y]+=1 
            y+=d
print(sum(v>1 for l in a for v in l ))
