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
s=b[0]

d={}
for v in a:
    x,_,y=v.split()
    d[x]=d.get(x,[])+[y]

#part 1
res=set()
for a in d:
    for i in range(len(s)):
        if s[i:][:len(a)]==a:
            for b in d[a]:
                x=s[:i]+b+s[i+len(a):]
                res|={x}

print(len(res))

#part 2
D={}
for a in d:
    for b in d[a]:
        D[b]=a

n=0
while s[1:]:
    for a in D:
        S=s.replace(a,D[a],1)
        n+=S!=s
        s=S
print(n)