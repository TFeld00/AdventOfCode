DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers


from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

e,r=parse_no_headers(r)

e=e[0]

def get_neigbors(d,y,x,default):
    for dy in (-1,0,1):
        for dx in (-1,0,1):
            X,Y=x+dx,y+dy
            yield d.get((Y,X),default)

d={}
for i,l in enumerate(r):
    for j,v in enumerate(l):d[(i,j)]=int(v=='#')

x,X,y,Y=0,len(r[0]),0,len(r)
def enhance(d,default):
    D={}
    a,b=zip(*d.keys())
    x,X,y,Y=min(a),max(a)+1,min(b),max(b)+1
    for i in range(y-1,Y+1):
        for j in range(x-1,X+1):
            s=0
            for n in get_neigbors(d,i,j,default):
                s*=2
                s+=n
            D[(i,j)]=int(e[s]=='#')
    return D


default=0
for _ in range(50):
    d=enhance(d,default)
    default =int(e[int(str(default)*9,2)]=='#')
    x-=1
    y-=1
    X+=1
    Y+=1
    if _ in (1,49):
        print(sum(d.values()))

