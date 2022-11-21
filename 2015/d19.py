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
        #l=l.split()
        #l=int(l)
        #l=list(l)
        #print(l)
        r+=[l]
        pass
#W,H=len(r[0]),len(r)

a,b=parse_no_headers(r)
s=b[0]

d={}
for v in a:
    x,_,y=v.split()
    d[x]=d.get(x,[])+[y]

#part 1
res=set()
for a in d:
    for i in range(len(s)):
        if s[i:][:len(a)]==a:
            for b in d[a]:
                x=s[:i]+b+s[i+len(a):]
                res|={x}

print(len(res))

#part 2
D={}
for a in d:
    for b in d[a]:
        D[b]=a

n=0
while s[1:]:
    for a in D:
        S=s.replace(a,D[a],1)
        n+=S!=s
        s=S
print(n)