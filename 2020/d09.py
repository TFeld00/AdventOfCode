import os
DAY,_,_=__file__.rpartition('.')

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=int(l),

W=25
for i in range(W,len(r)):
    x=r[i]
    s=set(r[i-W:i])
    f=0
    for j in range(W):
        y=r[i-j]
        if x-y in s and x-y!=y:f=1;break
    if not f:
        print(x)
        R=x
        break

def part2():
    for i in range(len(r)):
        s=r[i]
        for j in range(i+1,len(r)):
            s+=r[j]
            if s>R:break
            if s==R:
                return (min(r[i:j+1])+max(r[i:j+1]))

print(part2())