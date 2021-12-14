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
        pass

s,r=parse_no_headers(r)
s=s[0]

d={}
for l in r:
    a,b=l.split(' -> ')
    d[a]=b

def count(D):
    c={}
    for a,b in D:
        c[a]=c.get(a,0)+D[a+b]
        c[b]=c.get(b,0)+D[a+b]
    for v in c:
        c[v]=(c[v]+1)//2

    l=[(c[v],v)for v in c]
    a,b=max(l),min(l)
    print(a[0]-b[0])

D={}
for a,b in zip(s,s[1:]):
    c=a+b
    D[c]=D.get(c,0)+1
    
for t in range(40):
    D2={}
    for v in D:
        if v in d:
            a,b=v
            c=d[v]
            D2[a+c]=D2.get(a+c,0)+D[v]
            D2[c+b]=D2.get(c+b,0)+D[v]
        else:
            D2[v]=D[v]
    D=D2
    if t in (9,39):
        count(D)
