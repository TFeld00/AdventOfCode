DAY,_,_=__file__.rpartition('.')

from itertools import combinations

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

y=[]
x=[]
for i,l in enumerate(r):
    if '#'not in l:y+=i,
for i,l in enumerate(zip(*r)):
    if '#'not in l:x+=i,

p=[]
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='#':p+=[i,j],

def f(mult):
    s=0
    M=mult-1
    for (a,b),(c,d) in combinations(p,2):
        a,c=sorted([a,c])
        b,d=sorted([b,d])
        s+=abs(a-c)+abs(b-d) + sum(a<i<c for i in y)*M +sum(b<i<d for i in x)*M
    print(s)

f(2)
f(1000000)