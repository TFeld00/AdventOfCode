import os
DAY,_,_=__file__.rpartition('.')

r1=[]
r2=[]
r3=[]

s=0
r=r1
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        if l=='your ticket:':r=r2;continue
        if l=='nearby tickets:':r=r3;continue
        if l:
            r+=[l]

d={}
for l in r1:
    N,b=l.split(': ')
    x,_,y=b.split()
    a,b=map(int,x.split('-'))
    A,B=map(int,y.split('-'))
    d[N]=eval(f'lambda n:{a}<=n<={b} or {A}<=n<={B}')

r2=[[*map(int,t.split(','))]for t in r2]
r3=[[*map(int,t.split(','))]for t in r3]

def valid(n):
    for f in d.values():
        if f(n):return True
    return 0

s=0
for t in r3:
    for v in t:
        if not valid(v):
            s+=v
print(s)

r4 = [t for t in r3 if all(valid(v)for v in t)]
D={}

for i,l in enumerate(zip(*(r4+r2))):
    for s,f in d.items():
        if all(f(n) for n in l):
            D[s]=D.get(s,set())|{i}

# Clean
for v in sorted(D.values(),key=len):
    for s in D.values():
        if s!=v:
            s-=v
r=1
T=r2[0]
for s in D:
    if s.startswith('departure'):
        r*=T[D[s].pop()]
print(r)