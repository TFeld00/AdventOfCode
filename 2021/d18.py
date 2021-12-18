DAY,_,_=__file__.rpartition('.')

from functools import reduce
import re

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

def split(m):
    x=int(m[0])
    l=x//2
    r=x-l
    return str([l,r]).replace(' ','')

def expl_left(m,a):
    return str(int(m[0][::-1])+a)[::-1]

def red(s):
    S=s
    while 1:
        s=S
        stk=[]
        d=0
        e=0
        for i,c in enumerate(s):
            if c=='[':stk+=(i,c),;d+=1
            elif c==']':
                j,_=stk.pop()
                if d==5:
                    e=1
                    break
                d-=1
        if e:
            a,b = eval(s[j:i+1])
            x=re.sub('\d+',lambda m:expl_left(m,a),s[:j][::-1],1)[::-1]
            y=re.sub('\d+',lambda m:str(int(m[0])+b),s[i+1:],1)
            S=x+'0'+y
        else:
            S=re.sub('\d\d+',split,s,1)
        if S==s:
            return s

def add(a,b):
    r='['+red(a)+','+red(b)+']'
    r=red(r)
    return r

def mag(p):
    if type(p)==int:return p
    a,b=p
    return 3*mag(a)+2*mag(b)

#part 1
v=reduce(add,r)
print(mag(eval(v)))

#part 2
m=0
for a in r:
    for b in r:
        if a!=b:
            v=mag(eval(add(a,b)))
            m=max(v,m)
print(m)