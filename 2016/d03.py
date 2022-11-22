DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=[l]

#part 1
s=0
for v in r:
    a,b,c=sorted(v)
    s+=(a+b>c)
print(s)

#part 2
s=0
for l in zip(*r):
    for v in zip(*[iter(l)]*3):
        a,b,c=sorted(v)
        s+=(a+b>c)
print(s)