DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        d=1 if l[0]=='L' else -1
        v = int(l[1:])
        r+=[(d,v)]
        
        
# Part 1
t=0
i=50
for d,v in r:
    i+=d*v
    i%=100
    t+=i==0
print(t)

# Part 2

t=0
i=50
for d,v in r:
    for _ in range(v):
        i=(i+d)%100
        t+=i==0
print(t)