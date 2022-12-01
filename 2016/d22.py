DAY,_,_=__file__.rpartition('.')

import os
from itertools import *
from collections import *
_pow = pow
from math import *
pow = _pow
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, whitespace, punctuation, printable
from alg.dijkstra import dijkstra
from img.img import read_img, write_img, write_img_fromlist     #write_img(DAY,COLS)
from alg.util import parse_with_headers, parse_skip_headers, parse_no_headers, get_neigbors_both, get_neigbors_diag, get_neigbors_orto
from alg.floodfill import fill
from alg.cellular import step_dict, step_list, to_dict, to_lists
from alg.string import shift_caesar, tr, block_print
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
n=0
s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        #l=[*map(int,l.split())]
        #l=[*map(int,l)]
        l=l.split()
        #l=int(l)
        #l=list(l)
        #print(l)
        r+=[l]
        pass
#W,H=len(r[0]),len(r)

root,_,*r=r

#part 1
res=0
for n,s,u,a,p in r:
    u=int(u[:-1])
    if not u:continue
    for N,S,U,A,P in r:
        if n==N:continue
        A=int(A[:-1])
        res+=u<=A
print(res)

#part 2
d={}
for n,s,u,a,p in r:
    *_,x,y=n.split('-')
    x=int(x[1:])
    y=int(y[1:])
    s,u,a=int(s[:-1]),int(u[:-1]),int(a[:-1])
    d[(x,y)]=(u,s)

# TODO