DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]

        
def mix(n,v):
    return n^v

def prune(n):
    return n%16777216

def f(n):
    n=prune(mix(n,n*64))
    n=prune(mix(n,n//32))
    n=prune(mix(n,n*2048))
    return n

# part 1
res=0
for n in r:
    for _ in range(2000):
        n=f(n)
    res+=n

print(res)

# part 2

l=[]
res=0
total={}
for n in r:
    x=[n%10]
    dx=[]
    for _ in range(2000):
        n=f(n)
        dx+=(n%10)-x[-1],
        x+=n%10,
    xd=set()
    for i in range(len(x)-4):
        t=tuple(dx[i:i+4])
        if t not in xd:
            xd|={t}
            total[t]=total.get(t,0)+x[i+4]
    l+=xd,

print(max(total.values()))