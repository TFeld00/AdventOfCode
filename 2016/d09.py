DAY,_,_=__file__.rpartition('.')

from functools import cache

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

#part 1
i=0
l=0
while i<len(s):
    if s[i]=='(':
        j=i
        while s[j]!=')':j+=1
        x=s[i+1:j]
        a,b=map(int,x.split('x'))
        i=j+a+1
        l+=a*b
    else:
        i+=1
        l+=1
print(l)

#part 2
@cache
def f(s):
    i=0
    l=0
    while i<len(s):
        if s[i]=='(':
            j=i
            while s[j]!=')':j+=1
            x=s[i+1:j]
            a,b=map(int,x.split('x'))
            l+=f(s[j+1:j+1+a])*b
            i=j+a+1
        else:
            i+=1
            l+=1
    return l
print(f(s))