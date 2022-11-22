DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        n,_,_,a,_,_,b,*_,c,_=l.split()
        r+=[n,*map(int,(a,b,c))],

#part 1
t=2503
l=[]
for n,a,b,c in r:
    d=0
    x=b+c
    d+=a*(t//x)*b
    d+=a*min(b,t%x)
    l+=d,
print(max(l))

#part 2
p=[0]*len(r)
l=[0]*len(r)
for i in range(t):
    for j,(n,a,b,c) in enumerate(r):
        x=b+c
        if i%x<b:
            l[j]+=a
    m=max(l)
    for j,v in enumerate(l):
        if v==m:p[j]+=1
print(max(p))