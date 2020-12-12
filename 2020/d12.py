import os
DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        pass

D=1
X,Y=0,0
for s in r:
    c,n=s[0],int(s[1:])
    if c=='F':
        c='NESW'[D]
    elif c=='R':
        D=(D+n//90)%4
    elif c=='L':
        D=(D-n//90)%4
    if c=='N':
        Y-=n
    elif c=='S':
        Y+=n
    elif c=='E':
        X+=n
    elif c=='W':
        X-=n

print(abs(X)+abs(Y))


D=1
X,Y=0,0
wX,wY=10,-1
for s in r:
    c,n=s[0],int(s[1:])
    if c=='F':
        X+=wX*n
        Y+=wY*n
    elif c=='R':
        for i in range(n//90):
            wX,wY=-wY,wX
    elif c=='L':
        for i in range(n//90):
            wX,wY=wY,-wX
    elif c=='N':
        wY-=n
    elif c=='S':
        wY+=n
    elif c=='E':
        wX+=n
    elif c=='W':
        wX-=n

print(abs(X)+abs(Y))