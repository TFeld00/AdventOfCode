DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r={}
s=i=t=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split('|')
        x,y=a.split(':')
        w={*map(int,y.split())}
        n={*map(int,b.split())}
        a=len(n&w)
        #Part 1
        s+=(2**a)//2
        #Part 2        
        i+=1
        c=r.get(i,1)
        t+=c
        for j in range(i+1,i+a+1):
            r[j]=r.get(j,1)+c

print(s)
print(t)
