DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

x=y=0
T=[(0,0)]*9
v1={(0,0):1}
v9={(0,0):1}

for d,m in r:
    m=int(m)
    dx,dy={'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1),}[d]
    for _ in range(m):
        x+=dx
        y+=dy
        xp,yp=x,y
        for i,(xt,yt) in enumerate(T):
            if abs(xt-xp)+abs(yt-yp)>2:
                xt += 1 if xp>xt else -1
                yt += 1 if yp>yt else -1
            elif abs(xt-xp)>1:
                xt += 1 if xp>xt else -1
            elif abs(yt-yp)>1:
                yt += 1 if yp>yt else -1
            xp,yp=xt,yt
            T[i]=(xt,yt)
            if i==0:
                v1[(xt,yt)]=v1.get((xt,yt),0)+1
            elif i==8:
                v9[(xt,yt)]=v9.get((xt,yt),0)+1
print(len(v1))
print(len(v9))
