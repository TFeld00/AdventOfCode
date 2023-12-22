DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]
i=0
t=''
d={}
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        t+=l
        if 'S'in l:
            x=l.index('S')
            y=i
        i+=1

W,H=len(r[0]),len(r)

goal = 26501365

F=[3935, 34156, 94173] #precomputed

q={(x,y)}
i=0
while len(F)<3 or i<64:
    next=set()
    for x,y in q:
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if r[Y%H][X%W]in'.S':
                next|={(X,Y)}
    q=next
    if i%H==goal%H:
        F+=len(q),
    if i==63: #part 1
        print(len(q))
    i+=1

#part 2
a0,a1,a2 = F
b0 = a0
b1 = a1-a0
b2 = a2-a1
n=goal//H
print(b0 + b1*n + (n*(n-1)//2)*(b2-b1))

