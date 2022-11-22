DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

#part 1
x=y=1
for s in r:
    for c in s:
        if c=='U':y-=y>0
        elif c=='D':y+=y<2
        elif c=='L':x-=x>0
        else:x+=x<2
    print(end=['123','456','789'][y][x])

print()

#part 2
m=['  1',' 234','56789',' ABC','  D']
x,y=0,2
for s in r:
    for c in s:
        if c=='U':y-=y>abs(x-2)
        elif c=='D':y+=y<4-abs(x-2)
        elif c=='L':x-=x>abs(y-2)
        else:x+=x<4-abs(y-2)
    print(end=m[y][x])