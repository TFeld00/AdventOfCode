DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(', ')
        r+=l

d=0
v={(0,0)}
f=None
x=y=0
for c in r:
    t,i=c[0],int(c[1:])
    if t=='R':d+=1
    else:d-=1
    d%=4
    for _ in range(i):
        if d==0:y+=1
        elif d==1:x+=1
        elif d==2:y-=1
        else:x-=1
        if f==None and (x,y)in v:
            f=(abs(x)+abs(y))
        v|={(x,y)}

print(abs(x)+abs(y))

print(f)