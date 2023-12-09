DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=[l]
        
def f(r):
    s=0
    for l in r:
        x=[l]
        while len(set(l))>1:
            l=[b-a for a,b in zip(l,l[1:])]
            x+=l,
        while len(x)>1:
            w=x.pop()
            x[-1] += [x[-1][-1]+w[-1]]
        s+=x[-1][-1]
    print(s)

f(r)
f([l[::-1]for l in r])