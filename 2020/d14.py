import os
DAY,_,_=__file__.rpartition('.')

from functools import cache

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

mem={}

for l in r:
    if l[:4]=='mask':
        _,_,m=l.split()
        p,n=0,0
        for i,b in enumerate(m):
            p*=2;n*=2
            if b=='1':
                p+=1
            if b=='0':
                n+=1
        mask=m
    else:
        a,_,m=l.split()
        a=a[4:-1]
        a=int(a)

        m=int(m)
        m|=p
        m|=n
        m-=n
        mem[a]=m
print(sum(mem.values()))

@cache
def get(n,mask):
    l=len(n)
    if not l:return ['']
    if mask[-l]=='0':
        return [n[0]+v for v in get(n[1:],mask)]
    if mask[-l]=='1':
        return ['1'+v for v in get(n[1:],mask)]
    if mask[-l]=='X':
        return ['0'+v for v in get(n[1:],mask)]+['1'+v for v in get(n[1:],mask)]
    
mem={}

for l in r:
    if l[:4]=='mask':
        _,_,m=l.split()
        mask=m
    else:
        a,_,m=l.split()
        a=a[4:-1]
        a=int(a)
        m=int(m)
        
        for v in get(f'{a:036b}',mask):
            mem[int(v)]=m
            
print(sum(mem.values()))
