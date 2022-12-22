DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

m,ins=parse_no_headers(r)
ins=ins[0]

#part 1
def getMoves1():
    off={}
    maxlen=0
    for i,l in enumerate(m):
        left = len(l)-len(l.lstrip())
        right= len(l.rstrip())-1
        off[(i,left,2)] = (i,right,2)
        off[(i,right,0)] = (i,left,0)
        maxlen=max(maxlen,len(l))
    m2=[l.ljust(maxlen)for l in m]
    for i,l in enumerate(zip(*m2)):
        l=''.join(l)
        up = len(l)-len(l.lstrip())
        down= len(l.rstrip())-1
        off[(up,i,3)] = (down,i,3)
        off[(down,i,1)] = (up,i,1)
    return off

#part 2
def getMoves2():
    side = len(m[-1].strip())
    off={}
    for i in range(side):
        #6
        off[(0,side+i,3)]=(side*3+i,0,0)
        off[(side*3+i,0,2)]=(0,side+i,1)
        #7
        off[(0,side*2+i,3)]=(4*side-1,i,3)
        off[(4*side-1,i,1)]=(0,side*2+i,1)
        #4
        off[(i,side,2)]=(side*3-1-i,0,0)
        off[(side*3-1-i,0,2)]=(i,side,0)
        #2
        off[(i,side*3-1,0)]=(side*3-1-i,side*2-1,2)
        off[(side*3-1-i,side*2-1,0)]=(i,side*3-1,2)
        #1
        off[(side-1,side*2+i,1)]=(side+i,side*2-1,2)
        off[(side+i,side*2-1,0)]=(side-1,side*2+i,3)
        #3
        off[(side+i,side,2)]=(side*2,i,1)
        off[(side*2,i,3)]=(side+i,side,0)
        #5
        off[(side*3-1,side+i,1)]=(side*3+i,side-1,2)
        off[(side*3+i,side-1,0)]=(side*3-1,side+i,3)
    return off

# both parts
def run(off):
    left = len(m[0])-len(m[0].lstrip())
    x,y=left,0

    d=0
    move=lambda y,x,d:[(y,x+1,d),(y+1,x,d),(y,x-1,d),(y-1,x,d)][d]
    for i in re.findall(r'\d+|.',ins):
        if i.isdigit():
            i=int(i)
            for _ in range(i):
                Y,X,D=off.get((y,x,d),move(y,x,d))
                try:
                    if m[Y][X]=='.':
                        y,x,d=Y,X,D
                except: #for debugging
                    print(y,x,d,Y,X,D)
                    exit(0)
        elif i=='R':
            d=(d+1)%4
        else:
            d=(d-1)%4

    print((y+1)*1000+4*(x+1)+d)

#part 1
run(getMoves1())
#part 2
run(getMoves2())