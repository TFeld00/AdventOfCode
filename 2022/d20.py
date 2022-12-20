DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]


def run(part=1):
    m=[1,811589153][part-1]
    d={i:v*m for i,v in enumerate(r)}
    
    a=[*range(len(r))]

    for _ in range(1 if part==1 else 10):
        for n in range(len(r)):
            i=a.index(n)
            a=a[i+1:]+a[:i]
            v=d[n]%len(a)
            a[v:v]=[n]
    
    z=0
    for i in range(len(r)):
        if d[a[i]]==0:z=i

    print(sum(d[a[(z+o)%len(a)]] for o in (1000,2000,3000)))

run()
run(2)