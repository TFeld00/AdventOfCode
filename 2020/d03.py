import os
DAY,_,_=__file__.rpartition('.')

r=[]
s=0
i=0
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[[*l]]
        s+=l[i%len(l)]=='#'
        i+=3

print (s)

s2=1
for dx,dy in (1,1),(3,1),(5,1),(7,1),(1,2):
    xs=0
    x=y=0
    while y<len(r):
        l=r[y]
        xs+=l[x%len(l)]=='#'
        x+=dx
        y+=dy
    s2*=xs
print(s2)
