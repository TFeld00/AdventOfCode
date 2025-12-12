DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

*p,R=parse_no_headers(r)

def f(w,h,l):
    return sum(l)<=(w//3)*(h//3)

s=0
for r in R:
    d,*l = r.split()
    l=[*map(int,l)]
    w,h=[*map(int,re.findall(r'-?\d+',d))]
    s+=f(w,h,l)
print(s)