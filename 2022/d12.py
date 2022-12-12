DAY,_,_=__file__.rpartition('.')

from string import ascii_lowercase
from queue import Queue

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

d={c:ord(c) for c in ascii_lowercase}
d['S']=ord('a')
d['E']=ord('z')

def bfs(r,start,end,up):
    for i,l in enumerate(r):
        if start in l:
            x,y=l.find(start),i
            break
    W=len(r[0])
    H=len(r)
    q=Queue()
    s=set()
    q.put((x,y,0))
    while not q.empty():
        x,y,l=q.get()

        if r[y][x] in end:
            print(l)
            #WIN
            return l

        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue
            
            c=d[r[y][x]]
            if 0<=X<W and 0<=Y<H:
                o=d[r[Y][X]]
                if (up and o<=c+1) or (not up and o>=c-1):
                    s|={(X,Y)}
                    q.put((X,Y,l+1))

#part 1
bfs(r,'S','E',True)
#part 2
bfs(r,'E','Sa',False)



from img.img import write_img
COLS = {}
for c in ascii_lowercase:
    o=round((ord(c)-ord('a'))*255/26)
    COLS[c]=(o,o,o)
COLS['S']=(255,0,0)
COLS['E']=(0,255,0)
write_img(DAY,COLS)
