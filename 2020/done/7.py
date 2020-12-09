import os
DAY,_,_=__file__.rpartition('.')

d={}

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split(' bags contain ')
        b=b.split(', ')
        x=[]
        for o in b:
            o=o.split()
            if o[0].isdigit():
                if int(o[0])>0:
                    x+=(int(o[0]),' '.join(o[1:-1])),
        d[a]=x

d2={}
for a in d:
    for _,b in d.get(a,[]):
        d2[b]=d2.get(b,[])+[a]

q=['shiny gold']
r=[]
s=set()
while q:
    a=q.pop()
    for v in d2.get(a,[]):
        if v not in s:
            q+=[v]
        s|={v}
print(len(s-{'shiny gold'}))

def cont(b):
    r=1
    for n,o in d.get(b,[]):
        r+=n*cont(o)
    return r

print (cont('shiny gold')-1)