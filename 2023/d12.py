DAY,_,_=__file__.rpartition('.')

from functools import cache

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split()
        b=tuple([*map(int,b.split(','))])
        r+=[[a,b]]

@cache
def f(a,b):
    if not a:return int(not b)
    if not b:return int('#'not in a)
    if sum(b)+len(b)-1>len(a):return 0
    
    if a[0]=='.':
        return f(a[1:],b)
    if a[0]=='#':
        q=b[0]
        if all(a[i]in'?#'for i in range(q))and (q==len(a) or a[q]in'?.'):
            return f(a[q+1:],b[1:])
        return 0
    return f('#'+a[1:],b)+f(a[1:],b)

#part 1
s=0
for a,b in r:
    s+=f(a,b)
print(s)

#part 2
s=0
for a,b in r:
    a='?'.join([a]*5)
    b*=5
    s+=f(a,b)
print(s)
