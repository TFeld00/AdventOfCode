DAY,_,_=__file__.rpartition('.')

from itertools import *

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
        
W,H=len(r[0]),len(r)

d={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c!='.':
            d[c]=d.get(c,[])+[j*1j+i]


an=set()
for v,coords in d.items():
    for x,y in combinations(coords,2):
        p =  {x-(y-x), y+(y-x)}
        
        for a in p:
            X,Y = a.imag,a.real
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}


print(len(an))


an=set()
for v,coords in d.items():
    for x,y in combinations(coords,2):
        dx=y-x
        a=x
        while 1:
            X,Y = a.imag,a.real
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}
            else:break
            a-=dx
        a=x
        while 1:
            X,Y = a.imag,a.real
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}
            else:break
            a+=dx
        

print(len(an))

