DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        o,a,_,b=l.rsplit(' ',3)
        x,y,X,Y=map(int,a.split(',')+b.split(','))
        r+=[[o,x,X,y,Y]]


#part 1
m=[0]*1000000
for o,x,X,y,Y in r:
    f=[lambda n:n^1,lambda _:1,lambda _:0][(o=='turn on')-(o=='turn off')]
    for j in range(y,Y+1):
        for i in range(x,X+1):
            m[j*1000+i]=f(m[j*1000+i])

print(sum(m))

#part 2
m=[0]*1000000
for o,x,X,y,Y in r:
    f=[lambda n:n+2,lambda n:n+1,lambda n:max(0,n-1)][(o=='turn on')-(o=='turn off')]
    for j in range(y,Y+1):
        for i in range(x,X+1):
            m[j*1000+i]=f(m[j*1000+i])

print(sum(m))