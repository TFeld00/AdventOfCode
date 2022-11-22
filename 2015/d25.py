DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)


with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        *_,a,_,b=l.split()
        x,y=map(int,[a[:-1],b[:-1]])
        
n=m=0
d=x+y-2
while d:
    m+=1
    n+=m
    d-=1
i=n+y

#part 1
print((20151125*pow(252533,i-1,33554393))%33554393)

#slower ('brute force')
x=20151125
for _ in range(i-1):
    x=(x*252533)%33554393
print(x)
