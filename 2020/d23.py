import os
DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[*map(int,l)]


def move2(curr):
    a=next[curr]
    b=next[a]
    c=next[b]
    next[curr]=next[c]
    dest=curr-1
    while dest in (a,b,c)or dest <1:
        dest -=1
        if dest<1:dest=MAX
    ndest=next[dest]
    next[dest]=a
    next[c]=ndest
    return next[curr]

def list_nodes(curr):
    s=[curr]
    n=next[curr]
    while n!=curr:
        s+=n,
        n=next[n]
    return s

# Part 1
next={}
cups=r[:]
v1=curr=r[0]

for v in cups[1:]:
    next[v1]=v
    v1=v
next[v1]=curr
MAX=9

for i in range(100):
    curr=move2(curr)
s=''
l=list_nodes(1)
print(''.join(map(str,l[1:])))

#Part 2
next={}
cups=r[:]+[*range(10,1000001)]
v1=curr=r[0]

for v in cups[1:]:
    next[v1]=v
    v1=v
next[v1]=curr
MAX=1000000

for i in range(10000000):
    if i%100000==0:print(end='.')
    curr=move2(curr)
s=''

a=next[1]
b=next[a]
print(a,b)
print(a*b)