DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]


with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,_,b=l.split()

        x,y=map(int,a.split(','))
        X,Y=map(int,b.split(','))

        r+=[((x,y),(X,Y))]
        pass


a=[[0]*1000 for _ in range(1000)]
for (x,y),(X,Y)in r:
    if x==X or y==Y:
        x,X=sorted((x,X))
        y,Y=sorted((y,Y))
        for i in range(x,X+1):
            for j in range(y,Y+1):
                a[i][j]+=1

print(sum(v>1 for l in a for v in l ))



a=[[0]*1000 for _ in range(1000)]
for (x,y),(X,Y)in r:
    if x==X:
        y,Y=sorted((y,Y))
        for j in range(y,Y+1):
            a[x][j]+=1
    elif y==Y:
        x,X=sorted((x,X))
        for j in range(x,X+1):
            a[j][y]+=1
    else:
        (x,y),(X,Y)=sorted([(x,y),(X,Y)])
        d=1 if y<Y else -1
        for i in range(x,X+1):
            a[i][y]+=1 
            y+=d
print(sum(v>1 for l in a for v in l ))
