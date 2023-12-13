DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

L=parse_no_headers(r)
        
def f(M,ignore=0):
    for (v,m) in (1,M),(100,[*zip(*M)]):
        for i in range(1,len(m[0])):
            if all(all(x==y for x,y in zip(l[:i][::-1],l[i:])) for l in m):
                r=v*i
                if r!=ignore:
                    return r
    return 0

s1=0
s2=0
def g(m):
    global s1
    x=f(m)
    s1+=x
    for i,l in enumerate(m):
        for j,c in enumerate(l):
            w=[[*x]for x in m]
            w[i][j]='.#'[c=='.']
            q=f(w,x)
            if q:return q
    return 0
import time
a=time.time()
for m in L:
    m=[*map(list,m)]
    s2+=g(m)
b=time.time()
print(b-a)
print(s1)
print(s2)
