DAY,_,_=__file__.rpartition('.')

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split('|')
        l=[a.split(),b.split()]
        r+=[l]
        pass

s=0
for a,b in r:
    for d in b:
        s+=len(d) in(2,3,4,7)

print(s)

total=0
for a,b in r:
    d={}
    x=[{*v}for v in a+b]
    d[1]=next(v for v in x if len(v)==2)
    d[7]=next(v for v in x if len(v)==3)
    d[4]=next(v for v in x if len(v)==4)
    d[8]=next(v for v in x if len(v)==7)
    d[6]=next(v for v in x if len(v)==6 and d[1]-v)
    d[9]=next(v for v in x if len(v)==6 and v>d[4])
    d[0]=next(v for v in x if len(v)==6 and d[6]!=v!=d[9])
    d[5]=next(v for v in x if len(v)==5 and v<d[6])
    d[3]=next(v for v in x if len(v)==5 and d[5]!=v<d[9])
    d[2]=next(v for v in x if len(v)==5 and v not in d.values())
    s=''
    y={''.join(sorted(d[v])):str(v)for v in d}
    for v in b:
        s+=y[''.join(sorted(v))]
    total+=int(s)
print(total)