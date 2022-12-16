DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.split()
        r+=[l]
        pass

d={}
flow={}
for l in r:
    _,v,_,_,r,_,_,_,_,*t=l
    r=int(r[5:-1])
    t=[x.rstrip(',')for x in t]
    d[v]=t
    flow[v]=r

#part 1
q=[('AA',0,[])]
truncate = 1000

for t in range(30,0,-1):
    next=[]
    for p,s,o in q:
        if flow[p] and p not in o:
            next+=(p,s+(t-1)*flow[p],o+[p]),
        for x in d[p]:
            next+=[x,s,o],
    next.sort(key=lambda x:x[1],reverse=True)
    q=next[:truncate]

print(q[0][1])

#part 2
q=[('AA','AA',0,[])]
truncate = 2000

for t in range(26,0,-1):
    next=[]
    for p1,p2,s,o in q:
        if flow[p1] and p1 not in o:
            s1=s+(t-1)*flow[p1]
            o1=o+[p1]
            if flow[p2] and p2 not in o1:
                next+=[p1,p2,s1+(t-1)*flow[p2],o1+[p2]],
            for y in d[p2]:
                next+=[p1,y,s1,o1],
        elif flow[p2] and p2 not in o:
            s2=s+(t-1)*flow[p2]
            o2=o+[p2]
            for x in d[p1]:
                next+=[x,p2,s2,o2],
        for x in d[p1]:
            for y in d[p2]:
                next+=[x,y,s,o],
    next.sort(key=lambda x:x[2],reverse=True)
    q=next[:truncate]

print(q[0][2])