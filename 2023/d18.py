DAY,_,_=__file__.rpartition('.')

from img.img import write_img_fromlist
from alg.floodfill import fill
from alg.geom import area_pixels

COLS = {
    'a': (255, 255, 255),
    '#': (0, 0, 0),
    '.': (255, 0, 0),
}

from alg.file import download_input
download_input(DAY)

r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

def draw():
    M={}
    x=y=0
    for l in r:
        d,n,c=l
        n=int(n)
        if d=='U':
            for i in range(y-n,y):
                M[(i,x)]='#'
            y-=n
        elif d=='D':
            for i in range(y+1,y+n+1):
                M[(i,x)]='#'
            y+=n
        elif d=='L':
            for i in range(x-n,x):
                M[(y,i)]='#'
            x-=n
        elif d=='R':
            for i in range(x+1,x+n+1):
                M[(y,i)]='#'
            x+=n
    Y,X=zip(*M.keys())
    m=[]
    for i in range(min(Y)-1,max(Y)+2):
        l=[]
        for j in range(min(X)-1,max(X)+2):
            l+=M.get((i,j),'.'),
        m+=l,

    fill(m,(0,0),'a')
    write_img_fromlist(m,f'{DAY}',COLS)

def f(part):
    m=[]
    perim=0
    x=y=0
    for d,n,c in r:
        if part==1:
            d='RDLU'.find(d)
            n=int(n)
        else:
            d=int(c[7])
            n=int(c[2:7],16)

        perim+=n
        x,y=[[x+n,y],[x,y+n],[x-n,y],[x,y-n]][d]
        m+=[(x,y)]

    print(area_pixels(m))

f(1)
f(2)

draw()