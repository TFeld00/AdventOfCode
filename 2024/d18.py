DAY,_,_=__file__.rpartition('.')

from queue import *
import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=[l]
        

W=H=71
m=[['.']*W for _ in range(H)]

for x,y in r[:1024]:
    m[y][x]='#'


def bfs(r,x,y):
    W=len(r[0])
    H=len(r)
    q=Queue()
    s=set()
    q.put((x,y,0))
    while not q.empty():
        x,y,l=q.get()
        
        if (x,y)==(W-1,H-1):
            #print(l)
            #WIN
            return l
        
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue

            s|={(X,Y)}
            if 0<=X<W and 0<=Y<H:
                if r[Y][X]=='.':
                    q.put((X,Y,l+1))

print(bfs(m,0,0))

L,R=1024,len(r)
while L<R:
    w=(L+R)//2
    m=[['.']*W for _ in range(H)]
    for x,y in r[:w]:
        m[y][x]='#'
    if bfs(m,0,0):
        L=w+1
    else:
        R=w-1
print(','.join(map(str,r[L])))  