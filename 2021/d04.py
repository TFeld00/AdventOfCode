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
        #l=l.split()
        #l=int(l)
        #l=list(l)
        #print(l)
        r+=[l]
        pass
#W,H=len(r[0]),len(r)

n,*b=parse_no_headers(r)

b=[[[*map(int,l.split())]for l in x]for x in b]
n=[*map(int,n[0].split(','))]

def win(b,m):
    for r in b:
        if {*r}<={*m}:return 1
    for r in zip(*b):
        if {*r}<={*m}:return 1
    
def score(b,m):
    x=set(sum(b,[]))
    return sum(x-{*m})*m[-1]

#part1
def a():
    for i in range(len(n)):
        for B in b:
            if win(B,n[:i+1]):
                return score(B,n[:i+1])
print(a())

#part2
def a(b):
    for i in range(len(n)):
        w=[]
        for B in b:
            if win(B,n[:i+1]):
                w+=B,
                if len(b)==1:
                    break
        b=[B for B in b if B not in w]
        if not b:
            return [score(B,n[:i+1])for B in w]

print(a(b))


#alt
l=[]
for B in b:
    for i in range(len(n)):
        if win(B,n[:i+1]):
            l+=(i,score(B,n[:i+1])),
            break
l=[b for a,b in sorted(l)]
print(l[0],l[-1])