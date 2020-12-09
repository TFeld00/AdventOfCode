import os
DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

i=0
v=0
s=set()
while i<len(r):
    o,a=r[i]
    if i in s:print(v);break
    s|={i}
    a=int(a)
    if o=='acc':
        v+=a
    elif o=='jmp':
        i+=a-1
    elif o=='nop':
        pass
    i+=1

for x in range(len(r)):
    if r[x][0]=='acc':continue
    if r[x][0]=='jmp':r[x][0]='nop'
    elif r[x][0]=='nop':r[x][0]='jmp'

    i=0
    v=0
    s=set()
    inf=0
    while i<len(r):
        o,a=r[i]
        if i in s:inf=1;break
        s|={i}
        a=int(a)
        if o=='acc':
            v+=a
        elif o=='jmp':
            i+=a-1
        elif o=='nop':
            pass
        i+=1
    if r[x][0]=='jmp':r[x][0]='nop'
    elif r[x][0]=='nop':r[x][0]='jmp'

    if not inf:
        if i==len(r):
            print(v)
            break