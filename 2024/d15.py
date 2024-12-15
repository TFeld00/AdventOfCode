DAY,_,_=__file__.rpartition('.')

from img.img import write_img_fromlist
from alg.util import parse_no_headers

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
    '@': (255, 0, 0),
    'O': (115, 76, 54),
    '[': (115, 76, 54),
    ']': (163, 108, 77),
}

from alg.file import download_input
download_input(DAY)

r=[]
i=0
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[list(l)]
        if '@'in l:
            X,Y=l.find('@'),i
        i+=1
        
        
map,moves=parse_no_headers(r)
moves=''.join(''.join(x)for x in moves)

r=[l[:]for l in map]
W,H=len(r[0]),len(r)

def move(X,Y,m):
    dx,dy = [(0,-1),(0,1),(-1,0),(1,0)]['^v<>'.find(m)]
    x,y=X,Y
    while 0<=x<W and 0<=y<H:
        x+=dx
        y+=dy
        if r[y][x]=='.':
            #move
            while x!=X or y!=Y:
                r[y][x]=r[y-dy][x-dx]
                x-=dx;y-=dy
                r[y][x]='.'
                
            return X+dx,Y+dy
        elif r[y][x]=='#':
            return X,Y
            #stop


# pre moves:
write_img_fromlist(r,f"{DAY}_1a", COLS)

for m in moves:
    X,Y=move(X,Y,m)

s=0
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='O':
            s+=100*i+j
print(s)

#post moves
write_img_fromlist(r,f"{DAY}_1b", COLS)


# Part 2

r=[]
for l in map:
    x=[]
    for c in l:
        if c=='O':x+='[',']'
        elif c=='@':x+='@','.'
        else:x+=[c]*2
    r+=x,

for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='@':
            X,Y=j,i
            break


def move2(X,Y,m):
    dx,dy = [(0,-1),(0,1),(-1,0),(1,0)]['^v<>'.find(m)]

    q=[(X,Y,X+dx,Y+dy,'@')]
    
    for _,_,x,y,c in q:
        if r[y][x]=='#':
            # cannot move
            return X,Y
        elif r[y][x]=='[':
            q+=[x,y,x+dx,y+dy,'['],
            if dy:
                q+=[x+1,y,x+1+dx,y+dy,']'],
        elif r[y][x]==']':
            q+=[x,y,x+dx,y+dy,']'],
            if dy:
                q+=[x-1,y,x-1+dx,y+dy,'['],
    for x,y,X,Y,c in q[::-1]:
        r[y][x]='.'
        r[Y][X]=c
    return q[0][2:4]
            

# pre moves:
write_img_fromlist(r,f"{DAY}_2a", COLS)

for m in moves:
    X,Y=move2(X,Y,m)

s=0
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='[':
            s+=100*i+j
print(s)

# post moves
write_img_fromlist(r,f"{DAY}_2b", COLS)