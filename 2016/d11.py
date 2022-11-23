DAY,_,_=__file__.rpartition('.')

from itertools import *
from queue import *
import re

from alg.file import download_input
download_input(DAY)

r=[]
n=0
s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=re.findall(r'(\S+)( generator|-compatible microchip)',l)
        x=set()
        for a,b in l:
            x|={(a,b==' generator')}
        r+=[x]

def validFloor(f):
    for a,b in f:
        if not b and (a,True) not in f and any(y for x,y in f):
            return False
    return True

def valid(f,t,i):
    return validFloor(f-i) and validFloor(i) and validFloor(t|i)

def getState(e,r):
    d={}
    n=0
    s={}
    for i,f in enumerate(r):
        for a,b in f:
            s[a]=s.get(a,[0,0])
            s[a][b]=i
    for a in sorted(s,key=lambda v:s[v]):
        if a not in d:
            d[a]=n
            n+=1
    return (e,*[tuple(sorted((d[a],b)for a,b in f))for f in r])

def F(e,r):
    q=Queue()
    q.put((e,r,0))
    s=set()
    while not q.empty():
        e,r,m=q.get()
        R=getState(e,r)
        if R in s:continue
        s|={R}
        a,b,c,d=r
        if a==b==c==set():
            return m
        f=r[e]
        if e>0:
            t=r[e-1]
            down=0
            for x in 1,2:
                if down:break
                for i in combinations(f,x):
                    i=set(i)
                    if valid(f,t,i):
                        if e==1:
                            n=[a|i,b-i,c,d]
                            q.put((e-1,n,m+1))
                            down=1
                        if e==2:
                            if a or x>1:
                                n=[a,b|i,c-i,d]
                                q.put((e-1,n,m+1))
                                down=1
                        if e==3:
                            if a or b or x>1:
                                n=[a,b,c|i,d-i]
                                q.put((e-1,n,m+1))
                                down=1
        if e<3:
            t=r[e+1]
            up=0
            for x in 2,1:
                if up:break
                for i in combinations(f,x):
                    i=set(i)
                    if valid(f,t,i):
                        if e==0:
                            if c or d or x>1:
                                n=[a-i,b|i,c,d]
                                q.put((e+1,n,m+1))
                                up=1
                        if e==1:
                            if d or x>1:
                                n=[a,b-i,c|i,d]
                                q.put((e+1,n,m+1))
                                up=1
                        if e==2:
                            n=[a,b,c-i,d|i]
                            q.put((e+1,n,m+1))
                            up=1

print(F(0,r))

a,b,c,d=r
print(F(0,[a|{(x,y)for x in ('elerium','dilithium') for y in (False,True)},b,c,d]))
