DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
     
def f(M,target=0):
    for (v,m) in (1,M),(100,[*zip(*M)]):
        for i in range(1,len(m[0])):
            s=sum(sum(x!=y for x,y in zip(l[:i][::-1],l[i:])) for l in m)
            if s==target:
                return v*i
    return 0

s1=0
s2=0

for m in parse_no_headers(r):
    s1+=f(m,0)
    s2+=f(m,1)

print(s1)
print(s2)