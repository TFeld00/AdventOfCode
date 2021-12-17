DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

*_,x,y=r[0].split()
tx,tX=map(int,x[2:-1].split('..'))
ty,tY=map(int,y[2:].split('..'))

def steps(dx,dy):
    x,y=0,0
    m=0
    while x<=tX:
        x+=dx
        y+=dy
        dx-=[0,1,-1][(dx>0)-(dx<0)]
        dy-=1
        m=max(y,m)
        if tx<=x<=tX and ty<=y<=tY:return m
        if dx==0 and x<tx:break
        if y<ty:break
    return -1

m=0,0
s=0

for dx in range(tX+1):
    dy=ty-1
    for dy in range(ty-1,-ty):
        dy+=1
        r=steps(dx,dy)
        if r>=0:
            m=max((r,dy),m) # part 1
            s+=1            # part 2

print(m) #part 1
print(s) #part 2
