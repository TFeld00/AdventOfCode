DAY,_,_=__file__.rpartition('.')

from functools import *

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        *_,l=l.split()
        l=int(l)
        r+=[l]
        pass

H,D=r

@cache
def f(h,a,m,H,t,s,p,r,c,part=1):
    if part==2 and t==1:
        h-=1
        if h<=0:
            return(1,c)
    if r:m+=101
    if p:H-=3
    if s:a=7
    else:a=0
    s=max(0,s-1)
    p=max(0,p-1)
    r=max(0,r-1)
    if H<=0:
        return (0,c)
    if t:
        w=[(1,c)]
        if m>=53:
            w+=f(h,a,m-53,H-4,t^1,s,p,r,c+53,part),
        if m>=73:
            w+=f(h+2,a,m-73,H-2,t^1,s,p,r,c+73,part),
        if m>=113 and not s:
            w+=f(h,a,m-113,H,t^1,6,p,r,c+113,part),
        if m>=173 and not p:
            w+=f(h,a,m-173,H,t^1,s,6,r,c+173,part),
        if m>=229 and not r:
            w+=f(h,a,m-229,H,t^1,s,p,5,c+229,part),
        return min(w)
    else:
        h-=max(0,D-a)
        if h<=0:
            return (1,c)
        else:
            return f(h,a,m,H,t^1,s,p,r,c,part)

#part 1
print(f(50,0,500,H,1,0,0,0,0,1)[1])
#part 2
print(f(50,0,500,H,1,0,0,0,0,2)[1])