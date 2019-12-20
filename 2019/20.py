from intcode import *
from Queue import *
import sys

m=[]
with open('20.txt','r')as f:
 for l in f:
  m+=l.rstrip('\n'),

H,W=len(m),len(m[0])
portal={}
p2={}
for i,l in enumerate(m[:-1]):
    for j,c in enumerate(l[:-1]):
        if c.isalpha():
            if m[i+1][j].isalpha():
                P=c+m[i+1][j]
                if m[i-1][j]=='.':
                    r= -1 if i==H-2 else 1
                    p2[P]=p2.get(P,[])+[(j,i),(j,i-1,r)]
                elif m[i+2][j]=='.':
                    r= -1 if i==0 else 1
                    p2[P]=p2.get(P,[])+[(j,i+1),(j,i+2,r)]
            elif m[i][j+1].isalpha():
                P=c+m[i][j+1]
                if m[i][j-1]=='.':
                    r= -1 if j==W-2 else 1
                    p2[P]=p2.get(P,[])+[(j,i),(j-1,i,r)]
                elif m[i][j+2]=='.':
                    r= -1 if j==0 else 1
                    p2[P]=p2.get(P,[])+[(j+1,i),(j+2,i,r)]
p3={}
for v in p2:
    l=p2[v]
    if len(l)==4:
        a,b,c,d=l
        portal[a]=d
        portal[c]=b
    for a in l:
        p3[a[:2]]=v
        
start = p2['AA'][1]
end=p2['ZZ'][1]

def bfs((sx,sy,sr),(ex,ey,er),m,useR=0):
    q=Queue()
    q.put((sx,sy,0,0,[]))
    s=set()
    while not q.empty():
        x,y,l,r,qwe=q.get()
        for dx,dy in(-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            R=0
            if (X,Y,r)==(ex,ey,0):
                return l+1
            if(X,Y,r)in s:continue
            s|={(X,Y,r)}
            if (X,Y) in portal:
                X,Y,R=portal[X,Y]
                R*=useR
                if r+R<=0:
                    q.put((X,Y,l+1,r+R,qwe+[p3[X,Y]]))
            elif m[Y][X]=='.':
                q.put((X,Y,l+1,r,qwe))
            #|={(X,Y,r+R)}

print bfs(start,end,m)
print bfs(start,end,m,1)
