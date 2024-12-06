DAY,_,_=__file__.rpartition('.')

from img.img import read_img, write_img, write_img_fromlist     #write_img(DAY,COLS)
COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
    'O': (255, 0, 0),
    '^': (0, 255, 0),
}
from alg.file import download_input
download_input(DAY)

r=[]
s=0
t=''
i=0
y=x=0
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        if '^' in l:
            y=i
            x=l.find('^')
        i+=1
        
xInit,yInit = x,y
       
W,H=len(r[0]),len(r)
d=0
s=set()
p=[]
m=[(0,-1),(1,0),(0,1),(-1,0)]
while 0<=x<W and 0<=y<H:
    s|={(x,y)}
    p+=[(x,y,d)]
    dx,dy=m[d]
    X,Y=x+dx,y+dy
    if not (0<=X<W and 0<=Y<H):break
    while r[Y][X]=='#':
        d=(d+1)%4
        dx,dy=m[d]
        X,Y=x+dx,y+dy
        if not (0<=X<W and 0<=Y<H):break
    x,y=X,Y
    
print(len(s))

## draw
draw = [*map(list,r)]
for x,y in s:
    draw[y][x]='O'
draw[yInit][xInit]='^'
write_img_fromlist(draw,DAY+'_1',COLS)
##

#part 2
def hasLoop(r,x,y,d=0):
    s=set()
    p=[]
    m=[(0,-1),(1,0),(0,1),(-1,0)]
    while 0<=x<W and 0<=y<H:
        if (x,y,d) in s:return 1
        s|={(x,y,d)}
        p+=[(x,y,d)]
        dx,dy=m[d]
        X,Y=x+dx,y+dy
        if not (0<=X<W and 0<=Y<H):break
        while r[Y][X]=='#':
            d=(d+1)%4
            dx,dy=m[d]
            X,Y=x+dx,y+dy
            if not (0<=X<W and 0<=Y<H):break
        x,y=X,Y
    return 0

r2=0
r=[*map(list,r)]
draw = [*map(list,r)]
for j,i in s:
    c=r[i][j]
    if c!='.':continue
    r[i][j]= '#'
    if hasLoop(r,xInit,yInit):
        r2+=1
        draw[i][j]='O'
    r[i][j]=c
print(r2)

## draw
write_img_fromlist(draw,DAY+'_2',COLS)