import os
DAY,_,_=__file__.rpartition('.')

import re

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

r1=[]
r2=[]
r=r1
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        if not l:r=r2;continue
        r+=[l]
        pass


d={}
for v in r1:
    a,_,b=v.partition(': ')
    
    d[a]=b.replace('"','')

def get(n):
    r=d[n]
    
    if re.findall(r'\d',r):
        r=re.sub(r'\d+',lambda m:'('+get(m[0])+')',r)
    d[n]=r.replace(' ','')
    d[n]=re.sub(r'\(([a-z]+)\)',r'\1',d[n])
    return d[n]

rule=get('0')

s=0
for v in r2:
    if re.match('^('+rule+')$',v):s+=1
print(s)

d={}
for v in r1:
    a,_,b=v.partition(': ')
    
    d[a]=b.replace('"','')

d['8']='(42)+'
d['11']='(42 (42 (42 (42 (42 (42 31)? 31)? 31)? 31)? 31)? 31)'

rule=get('0')

s=0
for v in r2:
    if re.match('^('+rule+')$',v):s+=1
print(s)