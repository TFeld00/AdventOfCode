DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for i,l in enumerate(F):
        l=l.rstrip('\n')
        if 'S' in l:
            x,y = l.index('S'),i
        r+=[l]
        
        
W,H=len(r[0]),len(r)

s=0
s2=0

d={(x,y):1}
q=[(x,y)]
v=set()
for x,y in q:
    if (x,y) in v:continue
    v|={(x,y)}
    w=d[(x,y)]
    if r[y][x]=='^':
        s+=1
        q+=[(x-1,y+1),(x+1,y+1)]
        d[(x-1,y+1)]=d.get((x-1,y+1),0)+w
        d[(x+1,y+1)]=d.get((x+1,y+1),0)+w
    else:
        if y<H-1:
            q+=[(x,y+1)]
            d[(x,y+1)]=d.get((x,y+1),0)+w
        else:
            s2+=w

print(s)
print(s2)
