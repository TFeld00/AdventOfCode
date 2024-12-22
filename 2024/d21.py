DAY,_,_=__file__.rpartition('.')

import enum
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
from alg.grid import word_search, pattern_search
from alg.floodfill import fill, global_fill_dist, global_fill_dist_diags
from alg.cellular import step_dict, step_list, to_dict, to_lists, step_function_game_of_life
from alg.string import shift_caesar, tr, block_print, readable_number, findall_overlapping
from alg.geom import area, area_pixels
from functools import * # cmp_to_key etc..
from fractions import *
from textwrap import wrap
from datetime import *
from queue import *
import heapq #heapq.nsmallest
from functools import cache
import sympy    #sympy.primefactors, sympy.solve, sympy.sympify, etc..
import re
import sys
import z3
import networkx as nx

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
        
        
numpad=['789','456','123',' 0A']
keypad=[' ^A','<v>']


def bfs(s,r,x,y):
    W=len(r[0])
    H=len(r)
    res={''}
    for target in s:
        res2=set()
        q=Queue()
        s={(x,y):0}
        q.put((x,y,''))
        for i,l in enumerate(r):
            for j,c in enumerate(l):
                if c==target:
                    xt,yt=j,i
        minL=0
        while not q.empty():
            x,y,l=q.get()
            
            if (x,y)==(xt,yt):
                res2|={l+'A'}
                if not minL:minL=len(l)
                if minL<len(l):break
            
            for dx,dy,dt in (0,1,'v'),(0,-1,'^'),(1,0,'>'),(-1,0,'<'):
                X,Y=x+dx,y+dy
                if (X,Y)in s and s[(X,Y)]<len(l):continue

                s[(X,Y)]=len(l)
                if 0<=X<W and 0<=Y<H:
                    if r[Y][X]!=' ':
                        q.put((X,Y,l+dt))
        res={v+w for v in res for w in res2}
        x,y=xt,yt
    return res

def solve(s,levels):
    res=''

#    for c in s:
    r=bfs(s,numpad,2,3)
    m=min(map(len,r))
    r={v for v in r if len(v)==m}
    print(min(r),len(min(r)))
    for l in range(levels-1):
        r2=set()
        d2={}
        for v in r:
            w=bfs(v,keypad,2,0)
            d2[v]=min(map(len,w))
            r2|=w
        m=min(map(len,r2))
        r2={v for v in r2 if len(v)==m}
        r=r2
        print(min(r),len(min(r)))
    res+=r.pop()
    return len(res)

def f(m):
    d=len(re.findall('<+|>+|\^+|v+',m))
    c = [m.count(c)for c in '<v^>']
    return len(m),d,c

movesKey={}
for c1 in '<>v^A':
    for i,l in enumerate(keypad):
        for j,c in enumerate(l):
            if c==c1:x,y=j,i
    for c2 in '<>v^A':
        m=bfs(c2,keypad,x,y)
        movesKey[c1,c2]=m

print(movesKey)

movesNum={}
for c1 in '0123456789A':
    for i,l in enumerate(numpad):
        for j,c in enumerate(l):
            if c==c1:x,y=j,i
    for c2 in '0123456789A':
        m=bfs(c2,numpad,x,y)
        movesNum[c1,c2]=m

print(movesNum)
    
def solve2(s,levels):
    res=''
#    for c in s:
    r='A'+min(bfs(s,numpad,2,3),key=f)
    pairs={}
    for i in range(len(r)-1):
        p=r[i:i+2]
        pairs[p]=pairs.get(p,0)+1
    #print(pairs,sum(pairs.values()))
    for _ in range(levels-1):
        nextPairs={}
        for p,c in pairs.items():
            nxt='A'+min(movesKey[tuple(p)],key=f)
            for i in range(len(nxt)-1):
                p=nxt[i:i+2]
                nextPairs[p]=nextPairs.get(p,0)+c
        pairs=nextPairs
        #print(pairs,sum(pairs.values()))

    return sum(pairs.values())

@cache
def solve3(s,level,nums=1):
    if level==0:
        return len(s)
    moves = movesNum if nums else movesKey
    return sum(
        min(solve3(nxt, level - 1, 0) for nxt in moves[pair])
        for pair in zip('A' + s, s)
    )

res=0
for c in r:
    s1=solve3(c,3)
    s2=solve2(c,3)

    res+=s1*int(re.findall('\d+',c)[0])
    print(s1,int(re.findall('\d+',c)[0]))
print(res)


res=0
for c in r:
    s1=solve3(c,26)

    res+=s1*int(re.findall('\d+',c)[0])
#    print(s2,int(re.findall('\d+',c)[0]))
    print(s1,int(re.findall('\d+',c)[0]))
print(res)
