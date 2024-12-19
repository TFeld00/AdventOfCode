DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b=parse_no_headers(r)
a=a[0].split(', ')

d={}
def poss(s):
    if s=='':return 1
    if s in d:return d[s]
    x=0
    for t in a:
        if s.startswith(t):
            x+=poss(s[len(t):])
    d[s]=x
    return x

res1=0
res2=0
for v in b:
    res1+=poss(v)>0
    res2+=poss(v)

print(res1)
print(res2)