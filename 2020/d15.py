import os
DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=map(int,l.split(','))
        r+=l

d={}
i=0
p=0
for n in r:
    d[p]=i-1
    p=n
    i+=1

while i<30000000:
    a=d.get(p,i-1)
    n=i-a-1
    d[p]=i-1
    p=n
    i+=1
    if i==2020:print(p)
    if i%1000000==0:print(end='.')
print()
print(p)