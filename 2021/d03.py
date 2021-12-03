DAY,_,_=__file__.rpartition('.')


r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        pass

#part 1
v=w=0
for l in zip(*r):
    v*=2
    w*=2
    x=len(l)
    a=int(max ('01',key=l.count))
    v+=a
    w+=1-a
print(v*w)

#part 2
o=r[:]
i=0
while len(o)>1:
    l=[*zip(*o)][i]
    a=max ('01',key=l.count)
    if l.count('0')==l.count('1'):a='1'
    o=[v for v in o if v[i]==a]
    i+=1
o=int(o[0],2)

c=r[:]
i=0
while len(c)>1:
    l=[*zip(*c)][i]
    a=min ('01',key=l.count)
    if l.count('0')==l.count('1'):a='0'
    c=[v for v in c if v[i]==a]
    i+=1
c=int(c[0],2)

print(o*c)