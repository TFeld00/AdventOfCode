DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('-')
        r+=[l]

d={}
for a,b in r:
    d[a]=d.get(a,set())|{b}
    d[b]=d.get(b,set())|{a}

# Part 1
res=set()
for a in d:
    for b in d[a]:
        for c in d.get(b,[]):
            if c==a:continue
            if a in d.get(c,[]):
                res|={tuple(sorted((a,b,c)))}
s=0
for a,b,c in res:
    if 't' in a[0]+b[0]+c[0]:
        s+=1
print(s)

# Part 2
l=[{a}for a in d]
for a in d:
    for s in l:
        if s<=d[a]:
            s|={a}
m=max(l,key=len)
print(','.join(sorted(m)))