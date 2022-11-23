DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]


def val(v):
    if v.isalpha():
        return reg[v]
    return int(v)

def f():
    i=0
    while i<len(r):
        o,*l=r[i]
        if o=='cpy':
            x,y=l
            reg[y]=val(x)
        elif o=='inc':
            x=l[0]
            reg[x]+=1
        elif o=='dec':
            x=l[0]
            reg[x]-=1
        elif o=='jnz':
            x,y=l
            if val(x)!=0:
                i+=val(y)-1
        i+=1
    return(reg['a'])

#part 1
reg={'a':0,'b':0,'c':0,'d':0}
print(f())

#part 2
reg={'a':0,'b':0,'c':1,'d':0}
print(f())