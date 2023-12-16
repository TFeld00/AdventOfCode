DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
W,H=len(r[0]),len(r)

def f(x,y,d):
    s=set()
    q=[(x,y,d)]
    seen=set()
    for x,y,d in q:
        if (x,y,d)in seen:continue
        seen|={(x,y,d)}

        dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][d]
        x,y=x+dx,y+dy

        if 0<=x<W and 0<=y<H:
            s|={(x,y)}
        else:continue

        if r[y][x]=='/':
            d=[3,2,1,0][d]
            q+=[x,y,d],
        elif r[y][x]=='\\':
            d=[1,0,3,2][d]
            q+=[x,y,d],
        elif r[y][x]=='|':
            if d in [0,2]:
                q+=[x,y,1],
                q+=[x,y,3],
            else:     
                q+=[x,y,d],    
        elif r[y][x]=='-':
            if d in [1,3]:
                q+=[x,y,0],
                q+=[x,y,2],
            else:
                q+=[x,y,d],
        else:
            q+=[x,y,d],
    return len(s)

#Part 1
print(f(-1,0,0))

#Part 2
m=0
for i in range(H):
    a=f(-1,i,0)
    b=f(W,i,2)
    m=max(a,b,m)
for i in range(W):
    a=f(i,-1,1)
    b=f(i,H,3)
    m=max(a,b,m)
print(m)