DAY,_,_=__file__.rpartition('.')

from math import prod
from alg.util import parse_no_headers
import re

from alg.file import download_input
download_input(DAY)

r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
a,b=parse_no_headers(r)

d1={}
for l in a:
    n,l=l[:-1].split('{')
    d1[n]=l

""" Eval as functions
d={
    'A':(lambda v:True),
    'R':(lambda v:False)
    }
for l in a:
    n,l=l[:-1].split('{')
    d1[n]=l
    l=l.replace(',','\n else ')
    l=re.sub(r'([a-z])([<>]\d+:)([a-zA-Z]+)',r'if part["\1"]\2 return d["\3"](part)',l)
    l,x=l.rsplit(' ',1)
    l=l.replace('else if','elif')
    l='def f(part):\n '+l+': return d["'+x+'"](part)'
    exec(l)
    d[n]=f
    
s=0

for l in b:
    l=re.sub(r'([a-z])',r'"\1"',l)
    l=l.replace('=',':')
    l=eval(l)
    if d['in'](l):
        s+=sum(l.values())
print(s)
"""

def f(rule,d):
    R=d1[rule].split(',')
    if any(b<a for (a,b)in d.values()):return 0
    t=0
    for r in R:
        if ':'in r:
            l,r=r.split(':')
            c,o,n=l[0],l[1],int(l[2:])
            d={v:[*n]for v,n in d.items()}
            b={v:[*n]for v,n in d.items()}
            if o=='<':
                d[c][1]=min(d[c][1],n-1)
                b[c][0]=max(b[c][0],n)
            else:
                d[c][0]=max(d[c][0],n+1)
                b[c][1]=min(b[c][1],n)
        if r=='R':
            t+=0
        elif r=='A':
            t+=prod(max(0,v[1]-v[0]+1)for v in d.values())
        else:
            t+=f(r,d)
        d={v:[*n]for v,n in b.items()}

    return t

#part 1
s=0
for l in b:
    l={v:[int(n),int(n)]for v,n in zip('xmas',re.findall('\d+',l))}
    if f('in',l):
        s+=sum(x[0]for x in l.values())
print(s)

#part 2
print(f('in',{c:[1,4000]for c in 'xmas'}))
        

