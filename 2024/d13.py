DAY,_,_=__file__.rpartition('.')

from alg.util import parse_with_headers, parse_skip_headers, parse_no_headers
import re
import z3

from alg.file import download_input
download_input(DAY)

r=[]
s=0
t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=[l]
        
        
res = 0
for (x,y),(a,b),(q,z) in parse_no_headers(r):
    v=z3.Int('v')
    w=z3.Int('w')
    s=z3.Solver()
    s.add(v>=0, w>=0,v*x+w*a == q ,v*y+w*b == z, v<= 100, w<=100)
    if s.check()==z3.sat:
        a=s.model()
        res+=a[v]*3+a[w]
print(z3.simplify(res))


for (x,y),(a,b),(q,z) in parse_no_headers(r):
    v=z3.Int('v')
    w=z3.Int('w')
    s=z3.Solver()
    s.add(v>=0, w>=0,v*x+w*a == 10000000000000+q ,v*y+w*b == 10000000000000+z )
    if s.check()==z3.sat:
        a=s.model()
        res+=a[v]*3+a[w]
print(z3.simplify(res))