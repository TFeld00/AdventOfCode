DAY,_,_=__file__.rpartition('.')

from math import prod

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

v=0
z=[*zip(*r)]

for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c>max(l[:j]+'.') or c>max(l[j+1:]+'.') or c>max(z[j][:i]+('.',)) or c>max(z[j][i+1:]+('.',)):
            v+=1
print(v)

v=0
for i,l in enumerate(r):
    for j,c in enumerate(l):
        d=[]
        for s in (l[:j][::-1],l[j+1:],z[j][:i][::-1],z[j][i+1:]):
            x=0
            for x,y in enumerate(s,1):
                if y>=c:break
            d+=x,
        v=max(v,prod(d))
print(v)