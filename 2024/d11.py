DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=l
        
l={v:1 for v in r}
for i in range(75):
    if i==25: #part 1
        print(sum(l.values())) 
    
    n={}
    for s in l:
        c = l[s]
        x=str(s)
        w=len(x)
        if s==0:
            n[1] = n.get(1,0)+c
        elif w%2==0:
            a,b=int(x[:w//2]),int(x[w//2:])
            n[a] = n.get(a,0)+c
            n[b] = n.get(b,0)+c
        else:
            a=s*2024
            n[a] = n.get(a,0)+c

    l=n
print(sum(l.values()))