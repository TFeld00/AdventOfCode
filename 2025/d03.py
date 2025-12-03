DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l)]
        r+=[l]

def f(l,w):
    n=0
    i=0
    for e in range(w-1,-1,-1):
        a=max(l[i:-e or None])
        i=l[i:].index(a)+i+1
        n=10*n+a
    return n


s1=s2=0
for l in r:
    s1+=f(l,2)
    s2+=f(l,12)

print(s1)
print(s2)