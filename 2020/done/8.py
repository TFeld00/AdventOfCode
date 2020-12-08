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
    R=eval(str(r))
    if R[x][0]=='acc':continue
    if R[x][0]=='jmp':R[x][0]='nop'
    elif R[x][0]=='nop':R[x][0]='jmp'

    i=0
    v=0
    s=set()
    inf=0
    while i<len(R):
        o,a=R[i]
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
    if not inf:

        print(v)
        break