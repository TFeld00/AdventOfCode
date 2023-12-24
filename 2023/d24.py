DAY,_,_=__file__.rpartition('.')

from itertools import combinations
import re

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=[l]
        
        
interval=200000000000000 , 400000000000000
for a,b in combinations(r,2):
    x1,y1,z1,dx1,dy1,dz1=a
    x2,y2,z2=x1+dx1,y1+dy1,z1+dz1
    x3,y3,z3,dx3,dy3,dz3=b
    x4,y4,z4=x3+dx3,y3+dy3,z3+dz3
    D=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if D!=0:
        px=((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/D
        py=((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/D
        if (dx1<0 and px>x1) or (dx1>0 and px<x1)or (dy1<0 and py>y1) or (dy1>0 and py<y1) or \
            (dx3<0 and px>x3) or (dx3>0 and px<x3)or (dy3<0 and py>y3) or (dy3>0 and py<y3):
            continue
        if interval[0]<=px<=interval[1] and interval[0]<=py<=interval[1]:
            s+=1
print(s)


#part 2
import z3

I = lambda name: z3.Real(name)

x, y, z = I('x'), I('y'), I('z')
vx, vy, vz = I('vx'), I('vy'), I('vz')

s = z3.Solver()

for i, a in enumerate(r):
	ax, ay, az, vax, vay, vaz = a

	t = I(f't_{i}')
	s.add(t >= 0)
	s.add(x + vx * t == ax + vax * t)
	s.add(y + vy * t == ay + vay * t)
	s.add(z + vz * t == az + vaz * t)

assert s.check() == z3.sat

m = s.model()
x, y, z = m.eval(x), m.eval(y), m.eval(z)

print(eval(str(x + y + z)))