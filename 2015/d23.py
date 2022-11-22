DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[(l[:3],*l[4:].split(', '))]

def f(a,b):
    d={'a':a,'b':b}
    i=0
    while 0<=i<len(r):
        o,v,*w = r[i]
        i+=1
        if o=='hlf':
            d[v]//=2
        elif o=='tpl':
            d[v]*=3
        elif o=='inc':
            d[v]+=1
        elif o=='jmp':
            x=int(v)
            i+=x-1
        elif o=='jie':
            x=int(w[0])
            if d[v]%2==0:
                i+=x-1
        elif o=='jio':
            x=int(w[0])
            if d[v]==1:
                i+=x-1
    return d

#part 1
print(f(0,0)['b'])

#part 2
print(f(1,0)['b'])