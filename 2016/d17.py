DAY,_,_=__file__.rpartition('.')

from queue import *
from hashlib import md5

from alg.file import download_input
download_input(DAY)

r=[]
n=0
s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s=l

h = md5(str.encode(s,'ascii')).hexdigest()


def bfs(x,y,H,W):
    q=Queue()
    q.put((x,y,''))
    longest=0
    shortest=''
    while not q.empty():
        x,y,p=q.get()
        u,d,l,r = md5(str.encode(s+p,'ascii')).hexdigest()[:4]

        for dx,dy,o,m in (0,1,r,'R'),(0,-1,l,'L'),(1,0,d,'D'),(-1,0,u,'U'):
            if o>'a':
                X,Y=x+dx,y+dy

                if (X,Y)==(W-1,H-1):
                    if not shortest:
                        shortest=p+m
                    #WIN
                    longest=len(p+m)

                elif 0<=X<W and 0<=Y<H:
                        q.put((X,Y,p+m))
    print(shortest)
    print(longest)

bfs(0,0,4,4)
