DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

s=0
t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l
        
        
def f(v):
    n=0
    for c in v:
        n+=ord(c)
        n*=17
        n%=256
    return n

d=[[]for _ in range(256)]
for v in t.split(','):
    #part 1
    s+=f(v)

    #part 2
    l,v=re.split('[=-]',v)
    box=d[f(l)]
    if v:
        r=0
        for x in box:
            if x[0]==l:
                x[1]=int(v);r=1
        if not r:
            box+=[l,int(v)],
    else:
        for x in box:
            if x[0]==l:box.remove(x)

#part 1
print(s)

#part 2
s=0
for i,b in enumerate(d,1):
    for j,(_,v) in enumerate(b,1):
        s+=i*j*v
print(s)