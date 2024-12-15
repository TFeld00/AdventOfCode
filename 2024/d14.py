DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=[l]

W,H=101,103

q=[0,0,0,0]
for x,y,dx,dy in r:
    x=(x+dx*100)%W
    y=(y+dy*100)%H
    if x<W//2 and y<H//2:
        q[0]+=1
    elif x>W//2 and y<H//2:
        q[1]+=1
    elif x<W//2 and y>H//2:
        q[2]+=1
    elif x>W//2 and y>H//2:
        q[3]+=1
    
print(q[0]*q[1]*q[2]*q[3])

i=0
s=set()
all=[]
while 1:
    a=[]
    m=[list(' '*W) for _ in range(H)]

    for x,y,dx,dy in r:
        x=(x+dx*i)%W
        y=(y+dy*i)%H  
        m[y][x]='#'
        a+=[(x,y)]

    line = ''
    for l in m:
        line+=(''.join(l))+"\n"
    if '#'*20 in line:
        print(i)
        all+=(str(i)+'\n'),line
        break
    i+=1
    a=tuple(a)
    if a in s:break
    s|={a}

with open(f'{DAY}o.txt','w')as F:
    F.writelines(all)