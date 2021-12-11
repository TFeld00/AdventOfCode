DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=map(int,l)
        l=list(l)
        r+=[l]

def f(m):
    F=set()
    M=[[v+1 for v in l]for l in m]
    while 1:
        x=0
        for i,l in enumerate(M):
            for j,c in enumerate(l):
                if c>9:
                    for di in -1,0,1:
                        for dj in -1,0,1:
                            I,J=i+di,j+dj
                            if 0<=I<len(M) and 0<=J<len(M[0])and (I,J)not in F:
                                M[I][J]+=1
                    F|={(i,j)}
                    M[i][j]=0
                    x=1
        if not x:break
    return len(F),M

R=[l[:]for l in r]

s=0
for i in range(100):
    x,r=f(r)
    s+=x
print(s)

i=0
while 1:
    i+=1
    x,R=f(R)
    if x==len(R)*len(R[0]):break
print(i)
