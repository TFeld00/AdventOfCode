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
        l=l.split(' -> ')
        #l=int(l)
        #l=list(l)
        #print(l)
        r+=[[*map(eval,l)]]
        pass
#W,H=len(r[0]),len(r)

d={}
for l in r:
    for a,b in zip(l,l[1:]):
        x,y=a
        X,Y=b
        if x>X:x,X=X,x
        if y>Y:y,Y=Y,y
        for i in range(x,X+1):
            for j in range(y,Y+1):
                d[(i,j)]=1

x,y=zip(*d.keys())
lx,rx=min(x),max(x)
ly,ry=min(y),max(y)



m=[['.']*(rx-lx+1) for _ in range(0,ry+1)]
for x,y in d:m[y][x-lx]='#'

#write_img_fromlist(m,'2022/d14_1',COLS)

sx,sy=500-lx,0
minX=lx;maxX=rx
minY=ly;maxY=ry
w=maxX-minX+1
h=maxY+1

m[0][500-minX]='+'
g=0
stop=0
stack=[(500-minX,0)]
while not stop:
 x,y=500-minX,0
 g+=1
 end=0
 while y<maxY+2 and 0<=x<=w:
  if m[y+1][x]=='.':
   y+=1
  elif m[y+1][x]in'#s':
   if m[y+1][x-1]=='.':
    x-=1;y+=1
   elif m[y+1][x+1]=='.':
    x+=1;y+=1
   else:
     m[y][x]='s'
     end=1
     break
  else:
   if not end:stop=1
 if not end:stop=1


COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
    's': (255,255,0),
    '+': (0,255,0),
    ':': (255,0,0),
}
write_img_fromlist(m,'2022/d14_1',COLS)


t=0
s=set(d.keys())
while (500,0) not in s:
    x,y=(500,0)
    while 1:
        if y>maxY:break
        if (x,y+1)not in s:
            y+=1
        elif (x-1,y+1)not in s:
            x-=1
            y+=1
        elif (x+1,y+1)not in s:
            x+=1
            y+=1
        else:break
    s|={(x,y)}
    t+=1
print(t)