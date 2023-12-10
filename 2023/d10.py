DAY,_,_=__file__.rpartition('.')

from img.img import write_img_fromlist
from alg.floodfill import fill

COLS = {
    '.': (255, 255, 255),
    'o': (120, 120, 120),
    '#': (0, 0, 0),
    'S': (255, 0, 0),
}

from alg.file import download_input
download_input(DAY)

m=[]
x=y=0
with open(f'{DAY}.txt','r')as F:
    for i,l in enumerate(F):
        l=l.rstrip('\n')
        m+=[l]
        if 'S'in l:
            y=i
            x=l.find('S')

"""
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

# BFS
s=set()
q=[]
m2=[[*'.'*(len(m[0])*2+1)] for _ in range(len(m)*2+1)]
m2[y*2][x*2]='S'

def move(q,x,y,i):
    if m[y][x]in'S-J7'and x>0 and m[y][x-1]in'-LF' and (x-1,y)not in s:
        q+=[[x-1,y,i+1]]
        m2[y*2][(x-1)*2]='#'
        m2[y*2][(x)*2-1]='o'
    if m[y][x]in'S-LF'and x<len(m[y])-1 and m[y][x+1]in'-J7' and (x+1,y)not in s:
        q+=[[x+1,y,i+1]]
        m2[y*2][(x+1)*2]='#'
        m2[y*2][(x)*2+1]='o'
    if m[y][x]in'S|JL'and y>0 and m[y-1][x]in'|7F' and (x,y-1)not in s:
        q+=[[x,y-1,i+1]]
        m2[(y-1)*2][x*2]='#'
        m2[(y*2)-1][x*2]='o'
    if m[y][x]in'S|7F'and y<len(m)-1 and m[y+1][x]in'|JL' and (x,y+1)not in s:
        q+=[[x,y+1,i+1]]
        m2[(y+1)*2][x*2]='#'
        m2[(y*2)+1][x*2]='o'

move(q,x,y,0)
r=0
for x,y,i in q:
    s|={(x,y)}
    r=max(i,r)
    move(q,x,y,i)

#part 1
print(r)

#part 2
m2=[['.']+l+['.']for l in m2]
m2=[[*'.'*len(m2[0])]]+m2+[[*'.'*len(m2[0])]]
write_img_fromlist(m2,'2023/d10_1',COLS)

fill(m2,[0,0],'a')
write_img_fromlist(m2,'2023/d10_2',COLS)

m3=[l[1::2]for l in m2[1::2]]
write_img_fromlist(m3,'2023/d10_3',COLS)

#part 2 result
print(sum(l.count('.')for l in m3))