DAY,_,_=__file__.rpartition('.')

from itertools import pairwise
from img.img import write_img_fromlist
from alg.cellular import to_lists

from alg.file import download_input
download_input(DAY)

r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=[l]
        

# Part 1

a=0
for i,(x,y) in enumerate(r):
    for q,w in r[i:]:
        v=(abs(y-w)+1)*(abs(q-x)+1)
        a=max(a,v)
        
print(a)


# Part 2

# HOLE...
#94926
#48373
#50372

a=0
for i,(x,y) in enumerate(r):
    for q,w in r[i:]:
        x1,q1=(x,q) if x<=q else (q,x)
        y1,w1=(y,w) if y<=w else (w,y)
        if x1<94926 and q1>94926:continue
        if y1<48373 and w1>48373:continue
        if y1<50372 and w1>50372:continue
        
        if any((x1<a<q1) and (y1<b<w1) for a,b in r):continue
        v=(w1-y1+1)*(q1-x1+1)
        if v>a:
            X,Y,Q,W=x1,y1,q1,w1
            a=v

print(a)

## viz
d={}
if X>Q:X,Q=Q,X
if Y>W:Y,W=W,Y
X//=100
Y//=100
Q//=100
W//=100
for dx in range(X,Q+1):
    for dy in range(Y,W+1):
        d[(dx,dy)]='Y'
for (x,y),(q,w) in pairwise(r+r[:1]):
    if x>q:x,q=q,x
    if y>w:y,w=w,y
    x//=100
    y//=100
    q//=100
    w//=100
    
    d[(x,y)]='#'
    d[(q,w)]='#'
    for dx in range(x,q+1):
        for dy in range(y,w+1):
            d[(dx,dy)]='X'


L=to_lists(d,default='.')
COLS = {
    '.': (255, 255, 255),
    'X':(0,255,0),
    'Y':(0,0,255),
    '#': (255, 0, 0),
}
write_img_fromlist(L,DAY,COLS)