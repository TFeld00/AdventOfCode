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
from alg.util import parse_with_headers, parse_skip_headers, parse_no_headers
from alg.util import get_neigbors_both, get_neigbors_diag, get_neigbors_orto, get_neighbor_positions, get_neighbor_positions_complex
from alg.util import get_bounds, get_bounds_complex, get_bounds_complex_dict
from alg.util import rotate90clockwise, rotate180, rotate90counterclockwise
from alg.floodfill import fill
from alg.cellular import step_dict, step_list, to_dict, to_lists, step_function_game_of_life
from alg.string import shift_caesar, tr, block_print, readable_number, findall_overlapping
from alg.geom import area, area_pixels
from functools import *
from fractions import *
from textwrap import wrap
from datetime import *
from queue import *
import heapq
from functools import cache
import sympy    #sympy.primefactors, sympy.solve, sympy.sympify, etc..
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
t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        #l=[*map(int,l.split())]
        #l=[*map(int,l)]
        #l=l.split()
        #l=int(l)
        #l=list(l)
        #print(l)
        r+=[[*map(sorted,zip(l[:3],l[3:]))]]

r.sort(key=lambda b:b[2])
x,y,z=[max(map(max,l))for l in zip(*r)]
m={0:{}}
above={}
below={}
for brick,((x,X),(y,Y),(z,Z)) in enumerate(r):
    l=max(m)
    while not any(x<=a<=X and y<=b<=Y for a,b in m.get(l,{})) and l>0:
        l-=1
    l+=1
    on = {i for (a,b),i in m.get(l-1,{}).items()if x<=a<=X and y<=b<=Y}
    above[brick]=on
    for v in on:
        below[v]=below.get(v,set())|{brick}
    for i in range(Z-z+1):
        d=m.get(l+i,{})
        for j in range(x,X+1):
            for k in range(y,Y+1):
                d[(j,k)]=brick
        m[l+i]=d
    # print(brick,((x,X),(y,Y),(z,Z)))
    # if brick>2:break
# print(r)
# print(m)
s=0
for v in above:
    if all(len(above[w])>1 for w in below.get(v,set())):
        s+=1
print(s)
#print(above,below,sep='\n')

def fall(n):
    f={n}
    q=[n]
    for v in q:
        for w in below.get(v,set()):
            if above.get(w,set())<=f:
                f|={w}
                q+=w,
    return len(f)-1
print(sum(fall(v)for v in above))