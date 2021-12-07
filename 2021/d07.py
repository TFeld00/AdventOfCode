DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

r=[*map(int,r[0].split(','))]

x=sum(r)
for i in range(min(r),max(r)+1):
    d=sum(abs(b-i) for b in r)
    if d<x:x=d
print(x)


def f(n):
    return n*(n+1)//2

x=sum(map(f,r))
for i in range(min(r),max(r)+1):
    d=sum(f(abs(b-i)) for b in r)
    if d<x:x=d
print(x)