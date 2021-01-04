import os
DAY,_,_=__file__.rpartition('.')

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b=[*map(int,r)]

v=20201227

x=y=7
i=1
while x!=a and y!=b:
    i+=1
    x=(x*7)%v
    y=(y*7)%v

if x==a:
    print(pow(b,i,v))
else:
    print(pow(a,i,v))
