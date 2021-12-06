DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=map(int,l.split(','))
        r+=l
        pass

l=[0]*10
for f in r:
    l[f]+=1

for g in range(256):
    n=[0]*10
    for i,f in enumerate(l):
        if i:
            n[i-1]+=f
        else:
            n[6]+=f
            n[8]+=f
    l=n
    if g==79: #part 1
        print(sum(n))
print(sum(n))
