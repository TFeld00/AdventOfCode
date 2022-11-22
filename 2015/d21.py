DAY,_,_=__file__.rpartition('.')

from math import ceil

from alg.file import download_input
download_input(DAY)

r=[]
n=0
s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        *_,l=l.split()
        l=int(l)
        r+=[l]
        pass

H,D,A=r

h=100

wep = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
arm = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
ring = [(0,0,0,'A'),(0,0,0,'B'),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

w=[]
l=[]
for x in arm:
    for y in wep:
        for r1 in ring:
            for r2 in ring:
                if r1==r2:continue
                c=x[0]+y[0]+r1[0]+r2[0]
                d=y[1]+r1[1]+r2[1]
                a=x[2]+r1[2]+r2[2]
                t1=ceil(H/max(1,d-A))
                t2=ceil(h/max(1,D-a))
                if t1<=t2:w+=c,
                else:l+=c,
#part 1
print(min(w))
#part 2
print(max(l))