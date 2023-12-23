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
        r+=[l]
        t+=l
        
        
W,H=len(r[0]),len(r)

end=W-2,H-1

nodes={(1,0),(W-2,H-1)}
for i,l in enumerate(r[1:-1],1):
    for j,c in enumerate(l[1:-1],1):
        if r[i][j]!='#'and sum(v=='#' for _,_,v in get_neigbors_orto(r,i,j))<2:
            nodes|={(j,i)}

edges={}
for n in nodes:
    q=[(*n,0,{n})]
    for x,y,l,p in q:
        for X,Y,v in (x-1,y,'<.'),(x+1,y,'>.'),(x,y-1,'^.'),(x,y+1,'v.'):
            if (X,Y) not in p:
                if (X,Y)in nodes:
                    edges[n]=edges.get(n,[])+[((X,Y),l+1)]
                elif H>Y>=0<=X<W and r[Y][X]in v and (X,Y) not in p:
                    q+=[(X,Y,l+1,p|{(X,Y)})]

    
#part 1
m=0
q=[(1,0,0,[(1,0)])]
for x,y,l,p in q:
    for (X,Y),d in edges.get((x,y),[]):
        if (X,Y)==end:m=max(m,l+d)
        elif (X,Y) not in p:
            q+=[(X,Y,l+d,p+[(X,Y)])]
print(m)
