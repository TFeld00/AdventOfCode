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
        r+=[l]
#W,H=len(r[0]),len(r)


#First attempt: DFS (works for part 1)
@cache
def f(m,rO,rC,rOb,rG,o,c,ob,B):
    if m==1:return rG
    if m==0:return 0#rG
    nO,nC,nOb,nG=rO,rC,rOb,rG
    r=[]
    X=1
    mO=max(B[0],B[1],B[2],B[4])
    if o>=B[4] and ob>= B[5]:
        r+=f(m-1,rO,rC,rOb,rG+1,o+nO-B[4],c+nC,ob+nOb-B[5],B),
        X=0

    if X and m>1 and rOb<B[5] and o>=B[2] and c>= B[3]:
        r+=f(m-1,rO,rC,rOb+1,rG,o+nO-B[2],c+nC-B[3],ob+nOb,B),
        if rO>=mO:X=0

    if X and m>1 and rC<B[3] and o>=B[1]:
        r+=f(m-1,rO,rC+1,rOb,rG,o+nO-B[1],c+nC,ob+nOb,B),
        if rO>=mO:X=0

    if X and m>1 and rO<mO and o>=B[0]:
        r+=f(m-1,rO+1,rC,rOb,rG,o+nO-B[0],c+nC,ob+nOb,B),
        if rO>=mO:X=0

    if X:
        r+=f(m-1,rO,rC,rOb,rG,o+nO,c+nC,ob+nOb,B),
    return max(r)+nG

def h(state):
    (rO,rC,rOb,rG),(o,c,ob,g),(tO,tC,tOb,tG)=state
    return tG*10000+tOb*100+tC*10+tO

#part 2
def f2(steps,B):
    q=[((1,0,0,0),(0,0,0,0),(0,0,0,0))]

    for t in range(steps,0,-1):
        next=set()
        for (rO,rC,rOb,rG),(o,c,ob,g),(tO,tC,tOb,tG) in q:
            nO,nC,nOb,nG=rO,rC,rOb,rG

            total = (tO+nO,tC+nC,tOb+nOb,tG+nG)
            mO=max(B[0],B[1],B[2],B[4])
            if o>=B[4] and ob>= B[5]:
                next|={((rO,rC,rOb,rG+1),(o+nO-B[4],c+nC,ob+nOb-B[5],g+nG),total)}

            if t>1 and rOb<B[5] and o>=B[2] and c>= B[3]:
                next|={((rO,rC,rOb+1,rG),(o+nO-B[2],c+nC-B[3],ob+nOb,g+nG),total)}

            if t>1 and rC<B[3] and o>=B[1]:
                next|={((rO,rC+1,rOb,rG),(o+nO-B[1],c+nC,ob+nOb,g+nG),total)}

            if t>1 and rO<mO and o>=B[0]:
                next|={((rO+1,rC,rOb,rG),(o+nO-B[0],c+nC,ob+nOb,g+nG),total)}

            next|={((rO,rC,rOb,rG),(o+nO,c+nC,ob+nOb,g+nG),total)}
        q = sorted(next,key=h,reverse=True)[:1000]
    return max(q,key=h)[2][3]

#part 1
s=0
for i,*l in r:
    l=tuple(l)
    g=f2(24,l)
    s+=i*g
    print(i,g,sep=':',end=' ')
print()
print(s)

# #part 2
p=1
for i,*l in r[:3]:
    l=tuple(l)
    g=f2(32,l)
    p*=g
    print(i,g,sep=':',end=' ')
print()
print(p)