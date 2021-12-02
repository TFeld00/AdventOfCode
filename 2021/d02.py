DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

x=y=0

for d,n in r:
    n=int(n)
    if d[0]=='f':x+=n
    elif d[0]=='b':x-=n
    elif d[0]=='u':y-=n
    elif d[0]=='d':y+=n
print(x*y)


x=y=a=0

for d,n in r:
    n=int(n)
    if d[0]=='f':x+=n;y+=a*n
    elif d[0]=='b':x-=n;y-=a*n

    elif d[0]=='u':a-=n
    elif d[0]=='d':a+=n
print(x*y)