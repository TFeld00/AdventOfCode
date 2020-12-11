import os
DAY,_,_=__file__.rpartition('.')

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]
        pass


R=sorted(r)
R+=R[-1]+3,
d1=d2=d3=0
for a,b in zip([0]+R,R):
    x=b-a
    if x==1:d1+=1
    if x==2:d2+=1
    if x==3:d3+=1
print(d1*d3)

d={}
def f(r):
    if not r[1:]:return 1
    v=r[0]
    if v not in d:
        s=0
        if r[1:]and r[1]-v<4:
            s+=f(r[1:])
        if r[2:]and r[2]-v<4:
            s+=f(r[2:])
        if r[3:]and r[3]-v<4:
            s+=f(r[3:])
        d[v]=s
    return d[v]
print(f([0]+R))

d={0:1}
for v in R:
    d[v]=sum(d.get(v-1,0)+d.get(v-2,0)+d.get(v-3,0)
    #d[v]=sum(d.get(v-n,0)for n in(1,2,3))
print (d[R[-1]])
