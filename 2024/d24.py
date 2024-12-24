DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
import re

from alg.file import download_input
download_input(DAY)

r=[]
s=0
t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=re.findall('\w+',l)
        r+=[l]
        

A,B = parse_no_headers(r)

init={}

for x,y in A:
    init[x]=int(y)

def check(B):
    d=dict(init)
        
    q=B[:]
    seen=set()
    for a,o,b,c in q:
        if (a,o,b,len(d)) in seen:
            return ''
        if a in d and b in d:
            if o=='AND':
                r=d[a]&d[b]
            if o=='OR':
                r=d[a]|d[b]
            if o=='XOR':
                r=d[a]^d[b]

            d[c]=r
        else:
            q+=(a,o,b,c),
        seen|={(a,o,b,len(d))}

    s=''
    for v in sorted(d):
        if re.match('z\d\d',v):
            s+=str(d[v])

    return s

s=check(B)
print(int(s[::-1],2))

# Part 2
sx=sy=''
for v in sorted(init):
    if re.match('x\d\d',v):
        sx+=str(init[v])
    if re.match('y\d\d',v):
        sy+=str(init[v])
X,Y=int(sx[::-1],2),int(sy[::-1],2)

def swap(a,b):
    for x in B:
        if x[3]==a:
            for y in B:
                if y[3]==b:
                    x[3],y[3]=b,a
                    return

swap('gjc','qjj')
swap('wmp','z17')
swap('gvm','z26')
swap('qsb','z39')

d1={}
for a,o,b,c in B:
    d1[c]=[a,o,b]
d2={}
for a,o,b,c in B:
    a,b=sorted([a,b])
    d2[(a,o,b)]=c

Q=[]
for i in range(len(sx)):
    xi,yi=f'x{i:02}',f'y{i:02}'
    
    l=[
        (f'X{i:02}a',xi,'XOR',yi),
    ]
    if i:
        l+=[
            (f'A{i:02}a',xi,'AND',yi),
            (f'X{i:02}b',f'X{i:02}a','XOR',f'O{i-1:02}'),
            (f'A{i:02}b',f'X{i:02}a','AND',f'O{i-1:02}'),
            (f'O{i:02}',f'A{i:02}a','OR',f'A{i:02}b'),
        ]
    else:
        l+=[
            (f'O{i:02}',xi,'AND',yi),
        ]
    Q+=l

q=Q

d={}
d3={}
for i in range(5):
    q2=[]
    for x,X,O,Y in q:
        A1=d.get(X,X)
        B1=d.get(Y,Y)
        for (a,o,b),c in d2.items():
            if sorted([A1,B1])==sorted([a,b]) and O==o:
                d[x]=c
                d3[c]=x
                break
        if not x in d:
            q2+=[x,X,O,Y],
    q=q2
#     print(len(q))
#     print(len(d))

# print(d)
# print(q)

with open(f'{DAY}a.txt','w')as F:

    for a,o,b,c in B:
        F.write(' '.join([d3.get(a,a),o,d3.get(b,b),'->',d3.get(c,c),'\n']))



print(','.join(sorted(('gjc','qjj','wmp','z17','gvm','z26','qsb','z39'))))