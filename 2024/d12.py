DAY,_,_=__file__.rpartition('.')

from alg.floodfill import fill

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]


def calc(c,s):
    p=0
    for x,y in s:
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y) not in s:
                p+=1
    return p*c

def calc2(c,s):
    p=0
    # #side == #corners
    b=set()
    # Convex corners
    for x,y in s:
        a=[]
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            a+= (X,Y) not in s,
            if (X,Y) not in s:b|={(X,Y)}
        if a[0]and a[2]:p+=1
        if a[0]and a[3]:p+=1
        if a[1]and a[2]:p+=1
        if a[1]and a[3]:p+=1

    # Concave corners
    for x,y in b:
        a=[]
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            a+= (X,Y) in s,
        if a[0]and a[2] and (x+1,y+1) in s:p+=1
        if a[0]and a[3] and (x-1,y+1) in s:p+=1
        if a[1]and a[2] and (x+1,y-1) in s:p+=1
        if a[1]and a[3] and (x-1,y-1) in s:p+=1

    return p*c

res=0
res2=0
fv=0

for i,l in enumerate(r):
    for j,c in enumerate(l):
        if type(c)!=int:
            c,s=fill(r,(j,i),fv)
            fv+=1
            res += calc(c,s)
            res2 += calc2(c,s)

print(res)
print(res2)

