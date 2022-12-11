DAY,_,_=__file__.rpartition('.')

from math import prod,lcm
from alg.util import parse_no_headers

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        pass

r=parse_no_headers(r)

m={}
M=[]
l=[]
for g in r:
    a,b,c,d,e,f=g
    no=int(a.split()[-1][:-1])
    s=[*map(int,b.split(': ')[1].split(', '))]
    o = c.split(' = ')[1]
    o = eval('lambda old: '+o)
    div = int(d.split()[-1])
    toa = int(e.split()[-1])
    tob = int(f.split()[-1])
    M+=[o,div,toa,tob],
    m[no]=s
    l+=div,

l=lcm(*l)

def run(part,m,M):
    insp=[0]*len(M)
    for _ in range(20 if part == 1 else 10000):
        for mi,mon in enumerate(M):
            s=m[mi]
            o,d,a,b = mon
            for item in s:
                insp[mi]+=1

                if part==1:
                    w = o(item)//3
                else:
                    w = o(item)%l

                if w%d == 0:
                    m[a]+=[w]
                else:
                    m[b]+=[w]
            m[mi]=[]
            
    print(prod(sorted(insp)[-2:]))

run(1,eval(str(m)),M)
run(2,eval(str(m)),M)