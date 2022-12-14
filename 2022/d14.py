DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(' -> ')
        r+=[[*map(eval,l)]]

s=set()
maxY=0
for l in r:
    for a,b in zip(l,l[1:]):
        x,y=a
        X,Y=b
        if x>X:x,X=X,x
        if y>Y:y,Y=Y,y
        for i in range(x,X+1):
            for j in range(y,Y+1):
                s|={(i,j)}
            maxY=max(maxY,Y)

t1=t2=0
end1=0

start = (500,0)
while start not in s:
    x,y=start
    while 1:
        if y>maxY:
            end1=1
            break
        if (x,y+1)not in s:
            y+=1
        elif (x-1,y+1)not in s:
            x-=1
            y+=1
        elif (x+1,y+1)not in s:
            x+=1
            y+=1
        else:break
    s|={(x,y)}
    if not end1:t1+=1
    t2+=1

print(t1)
print(t2)
