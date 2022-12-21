DAY,_,_=__file__.rpartition('.')

from functools import *
import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,*l=l.split()
        a=a[:-1]
        r+=[a,*l],

d={}
for m,*l in r:
    d[m]=l

#part 1
@cache
def f(m):
    l=d[m]
    if len(l)==1:
        return l[0]
    else:
        a,o,b = l
        return int(eval(f'{f(a)}{o}{f(b)}'))

print(f('root'))


#part 2
a,_,b=d['root']

@cache
def f(m):
    if m=='humn':return 'x'
    l=d[m]
    if len(l)==1:
        return l[0]
    else:
        a,o,b = l
        s=f'({f(a)}{o}{f(b)})'
        if 'x' not in s:
            return int(eval(s))
        return s

x,y=f(a),f(b)
if type(x)==int:
    s,v=y,x
else:
    s,v=x,y

r=v
while '('in s:
    a,o,b,A,O,B=re.match('^(\d+)([+\-*/])(.*)$|^(.+)([+\-*/])(\d+)$',s[1:-1]).groups()
    if not a:
        a,o,b=A,O,B

    if 'x'in a:s=a
    else:s=b

    if o=='+':
        if 'x'in a:
            r=f'{r}-{b}'
        else:
            r=f'{r}-{a}'
    elif o=='-':
        if 'x'in a:
            r=f'{r}+{b}'
        else:
            r=f'{a}-{r}'
    elif o=='*':
        if 'x'in a:
            r=f'{r}//{b}'
        else:
            r=f'{r}//{a}'
    elif o=='/':
        if 'x'in a:
            r=f'{r}*{b}'
        else:
            r=f'{a}//{r}'

    r=eval(r)
print(r)