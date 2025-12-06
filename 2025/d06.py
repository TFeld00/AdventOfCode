DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from alg.file import download_input
download_input(DAY)

# Part 1
r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

s=0
for *l,o in zip(*r):
    s+=eval(o.join(l))
print(s)

# Part 2
r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]

r=[v if any(x!=' 'for x in v) else [] for v in zip(*r)]

s=0
for x,*l in parse_no_headers(r):
    *a,o=x
    l=[a,*l]
    s+=eval(o.join(''.join(x)for x in l))
print(s)