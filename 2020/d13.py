import os
DAY,_,_=__file__.rpartition('.')

from itertools import *
from collections import *
from math import *
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, whitespace, punctuation, printable
from alg.dijkstra import dijkstra
from img.img import read_img, write_img     #write_img(DAY)
from fractions import *
from queue import *
import sympy
import re
import sys

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

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

t=int(r[0])
B=r[1].split(',')

b1=[int(x)for x in B if x.isdigit()]

A=[]
for x in b1:
    a=t//x
    X,Y=a*x,(a+1)*x
    if X==t:A+=[(X,x)]
    else:A+=[(Y,x)]
a,b=min(A)
print((a-t)*b)

B=r[1].split(',')
B1 = []
for i,v in enumerate(B):
    if v.isdigit():
        B1+=[int(v),-i]
# print(B1)
# r=a*17-0
# =b*37-11
# =c*907-17
# =d*19-29
# =e*23-40
# =f*29-46
# =g*653-48
# =h*41-58
# =i*13-61

#https://www.wolframalpha.com/input/?i=r%3Da*17-0+%3Db*37-11+%3Dc*907-17+%3Dd*19-29+%3De*23-40+%3Df*29-46+%3Dg*653-48+%3Dh*41-58+%3Di*13-61

n=0
a = 148022875403143* n + 49540363913054#, b = 68010510320363 n + 22761788824917, c = 2774408910533 n + 928540448205, d = 132441520097549 n + 44325588764313, e = 109408212254497 n + 36616790718346, f = 86772030408739 n + 29040902983516, g = 3853581748627 n + 1289718509222, h = 61375338581791 n + 20541126500536, i = 193568375527187 n + 64783552809383, n element Z
r=a*17
print(r)

# Method 2
from sympy.ntheory.modular import crt
U,M=[],[]

R,M=zip(*[(-i,int(v))for i,v in enumerate(B)if v.isdigit()])
print(crt(M,R))


# Method 3
step=1
n=0
for i,v in enumerate(B):
    if v.isdigit():
        offset=i
        v=int(v)
        while (n+i)%v:
            n+=step
        step*=v
#        step=lcm(step,v)
print(n)