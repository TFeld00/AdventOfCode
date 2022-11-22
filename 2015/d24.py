DAY,_,_=__file__.rpartition('.')

from math import prod
from itertools import *

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]
        pass

r=set(r)

def f(s):
    x=0
    e=[]
    for i in range(1,len(r)):
        for c in combinations(r,i):
            if sum(c)==s:
                e+=prod(c),
                x=1
        if x:break
    return min(e)

print(f(sum(r)//3))

print(f(sum(r)//4))