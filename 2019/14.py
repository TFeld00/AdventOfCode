
D={'ORE':[1,[]]}
with open('14.txt','r')as f:
    for l in f:
        a,b=l.strip().split(' => ')
        a=a.split(', ')
        x,b=b.split()
        x=int(x)
        a=[s.split()for s in a]
        a=[[y,int(v)]for v,y in a]
        D[b]=[x,a]

C={}
P={}
def react(s,v):
    x,n=D[s]
    v=max(0,v-C.get(s,0))
    m=-(v/-x)
    for t,y in n:
        react(t,y*m)
        C[t]-=y*m
    C[s]=C.get(s,0)+m*x
    P[s]=P.get(s,0)+m*x

#PART 1
react('FUEL',1)
print P['ORE']

#PART 2
x=1000000000000

l,r=1,x
while l<r-1:
    C={}
    P={}
    m=(l+r)/2
    react('FUEL',m)
    B=P['ORE']
    if B<x:l,r=m,r
    else:l,r=l,m

print l
