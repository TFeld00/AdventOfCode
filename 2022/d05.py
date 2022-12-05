DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b = parse_no_headers(r)

a=[*zip(*a)][1::4]

def solve(part = 1):
    d = -1 if part ==1 else 1
    
    l=[]
    for v in a:
        n,*v = v[::-1]
        l+=[c for c in v if c!=' '],

    for m in b:
        _,n,_,x,_,y=m.split()
        n,x,y=map(int,[n,x,y])
        x-=1
        y-=1
        m=l[x][-n:]
        l[x]=l[x][:-n]
        l[y]+=m[::d]

    print(*[v[-1]for v in l],sep='')

solve(1)
solve(2)