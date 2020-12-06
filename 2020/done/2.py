import os
DAY,_,_=__file__.rpartition('.')

s=0
s2=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        a,b,c=l.split()
        x,y=map(int,a.split('-'))
        b=b[:-1]
        s+= x<=c.count(b)<=y
        s2+= (c[x-1:x]==b)^(c[y-1:y]==b)

print(s)
print(s2)
