DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]


class Node:
    def __init__(self, val, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt

def part(p,r):
    m=1 if p==1 else 811589153
    r=[Node(v*m)for v in r]
    for a,b in zip(r,r[1:]+r[:1]):
        a.nxt=b
        b.prv=a

    for _ in range(1 if p==1 else 10):
        for v in r:
            c=v

            c.prv.nxt=c.nxt
            c.nxt.prv=c.prv

            a=c.prv
            b=c.nxt
            for _ in range(c.val%(len(r)-1)):
                a=a.nxt
            b=a.nxt
            
            a.nxt=c
            c.prv=a
            b.prv=c
            c.nxt=b

    for x in r:
        if x.val == 0:
            r = 0
            y = x
            for _ in range(3):
                for _ in range(1000):
                    y = y.nxt
                r += y.val
            print(r)
        
part(1,r)
part(2,r)