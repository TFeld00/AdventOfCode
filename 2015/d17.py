DAY,_,_=__file__.rpartition('.')

from itertools import *

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]

#part 1
x=0
for i in range(len(r)):
    for c in combinations(r,i+1):
        x+=sum(c)==150
print(x)

#part 2
x=0
for i in range(len(r)):
    for c in combinations(r,i+1):
        x+=sum(c)==150
    if x:break
print(x)