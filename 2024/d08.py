DAY,_,_=__file__.rpartition('.')

from itertools import *

from sympy import Point

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
        
W,H=len(r[0]),len(r)


#region Complex
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


#endregion

#region coords
d={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c!='.':
            d[c]=d.get(c,[])+[(j,i)]


an=set()
for v,coords in d.items():
    for (x,y),(i,j) in combinations(coords,2):
        dx = i-x      
        dy=j-y
        p1=(x-dx,y-dy)
        p2=(i+dx,j+dy)
        for X,Y in p1,p2:
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}


print(len(an))

an=set()
for v,coords in d.items():
    for (x,y),(i,j) in combinations(coords,2):
        dx=i-x      
        dy=j-y
        X,Y=x,y
        while 1:
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}
            else:break
            X-=dx
            Y-=dy
        X,Y=x,y
        while 1:
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}
            else:break
            X+=dx
            Y+=dy
        

print(len(an))
#endregion


#region Point
d={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c!='.':
            d[c]=d.get(c,[])+[Point(j,i)]

an=set()
for v,coords in d.items():
    for x,y in combinations(coords,2):
        p =  {x-(y-x), y+(y-x)}
        
        for a in p:
            X,Y = a
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}


print(len(an))


an=set()
for v,coords in d.items():
    for x,y in combinations(coords,2):
        dx=y-x
        a=x
        while 1:
            X,Y = a
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}
            else:break
            a-=dx
        a=x
        while 1:
            X,Y = a
            if 0<=X<W and 0<=Y<H:
                an|={(X,Y)}
            else:break
            a+=dx
        

print(len(an))


#endregion
