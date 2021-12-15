DAY,_,_=__file__.rpartition('.')

from alg.dijkstra import dijkstra, get_dijkstra_path
from img.img import write_img_fromlist     #write_img(DAY,COLS)
from alg.util import get_neigbors_orto

COLS = {
    '.': (80, 80, 80),
    '1': (0, 100, 255),
    '2': (0, 255, 100),
}

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=map(int,l)
        l=list(l)
        r+=[l]
        pass
W,H=len(r[0]),len(r)

#part 1
#build graph
d={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        
        d[(i,j)]={(x,y):v for y,x,v in get_neigbors_orto(r,j,i)}

#dijkstra
D1=dijkstra(d, (0,0))
print(D1[(W-1,H-1)] [0])


#part 2
#extend input
R=[]
for j in range(5):
    for _,l in enumerate(r):
        R+=sum([[(v+i+j)%9 or 9 for v in l]for i in range(5)],[]),

#build graph
d={}
for i,l in enumerate(R):
    for j,c in enumerate(l):        
        d[(i,j)]={(x,y):v for y,x,v in get_neigbors_orto(R,j,i)}

#dijkstra
D2=dijkstra(d, (0,0))
w,h=len(R[0]),len(R)
print(D2[(w-1,h-1)][0])

#viz
m=[['.']*w for _ in' '*h]
for x,y in get_dijkstra_path(D1,(W-1,H-1)):
    m[y][x]='1'

for x,y in get_dijkstra_path(D2,(w-1,h-1)):
    m[y][x]='2'

write_img_fromlist(m,DAY,COLS)