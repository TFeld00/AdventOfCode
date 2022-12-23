DAY,_,_=__file__.rpartition('.')

from alg.util import get_neighbor_positions_complex, get_bounds_complex
from alg.file import download_input
download_input(DAY)

elves=set()
with open(f'{DAY}.txt','r')as F:
    y=0
    for l in F:
        l=l.rstrip('\n')
        for x,c in enumerate(l):
            if c=='#':
                elves|={x+1j*y}
        y+=1

def has_neigbors(m, p):
    for P in get_neighbor_positions_complex(p,False):
        if P in m:return True
    return False

#       north            south             west            east
d=(-1-1j,-1j,1-1j), (-1+1j,1j,1+1j), (-1-1j,-1,-1+1j), (1-1j,1,1+1j)
di=0

r=0
while 1:
    r+=1
    m={}
    mc={}
    for e in elves:
        if has_neigbors(elves,e):
            for _ in d[di:]+d[:di]:
                a,b,c=_
                if not {e+a,e+b,e+c} & elves:
                    m[e]=e+b
                    mc[e+b]=mc.get(e+b,0)+1
                    break
    di=(di+1)%4
    e2=set()
    for e in elves:
        v=0
        if e in m:
            n = m[e]
            if mc[n]==1:
                e2|={n}
                v=1
        if not v:
            e2|={e}

    if elves==e2:break #part 2
    elves=e2
    if r==10: #part 1
        x,X,y,Y=get_bounds_complex(elves)
        print((X-x+1)*(Y-y+1)-len(elves))
    
print(r)