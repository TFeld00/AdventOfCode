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
s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

#part 1
print(s.count('(')-s.count(')'))

#part 2
l=0
for i,c in enumerate(s,1):
    if c=='(':l+=1
    else:l-=1
    if l<0:break
print(i)