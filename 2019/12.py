M=[]
with open('12.txt','r')as f:
 for l in f:
  l=l.strip()[1:-1].split(',')
  m=[]
  for v in l:
    m+=[int(v.split('=')[1])]
  M+=[m+[0,0,0]]

def step(m):
    for i in range(3):
        for j in range(i+1,4):
            a,b=m[i],m[j]
            for d in range(3):
                if a[d]<b[d]:
                    a[d+3]+=1;b[d+3]-=1
                elif a[d]>b[d]:
                    a[d+3]-=1;b[d+3]+=1

    for i in range(4):
        for d in range(3):
            m[i][d]+=m[i][d+3]
    return m


#PART 1
m=eval(str(M))

for _ in xrange(1000):
    m=step(m)
E=0

for x in m:
    p=sum(map(abs,x[:3]))
    k=sum(map(abs,x[3:]))
    E+=p*k

print E

#PART 2
from fractions import *

def lcm(a,b):
    return abs(a*b)/gcd(a,b)

sx=set()
sy=set()
sz=set()
i=0
X,Y,Z=0,0,0

m=eval(str(M))
while 1:
    m=step(m)
    A,B,C,a,b,c=zip(*m)
    a,b,c=A+a,B+b,C+c
    if a in sx and not X:X=i
    if b in sy and not Y:Y=i
    if c in sz and not Z:Z=i
    sx|={a}
    sy|={b}
    sz|={c}
    i+=1
    if X*Y*Z:break

print lcm(lcm(X,Y),Z)
