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
for n in r:
    v=d.get(n,[i,i])
    d[n]=[v[1],i]
    p=n
    i+=1

while i<30000000:
    a,b=d[p]
    n=b-a
    p=n
    a,b=d.get(n,(i,i))
    d[n]=(b,i)
    i+=1
    if i==2020:print(p)
    if i%1000000==0:print(end='.')
print()
print(p)