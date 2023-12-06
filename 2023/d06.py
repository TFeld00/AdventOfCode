DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

r1=[]
r2=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r1+=[*map(int,re.findall('-?\d+',l))],
        l=l.replace(' ','')
        r2+=[*map(int,re.findall('-?\d+',l))],

def f(r):
    p=1
    for a,b in zip(*r):
        v=0
        for i in range(0,a+1):
            s=i
            d=(a-i)*s
            v+=d>b
        p*=v
    print(p)

f(r1)
f(r2)