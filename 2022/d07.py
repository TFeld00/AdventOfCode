DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

d={'/':{}}
path=[]
curr=d
for a,*l in r:
    if a=='$':
        b,*l=l
        if b=='cd':
            c=l[0]
            if c=='..':
                curr=path.pop()
            else:
                path+=curr,
                curr=curr[c]

    else:
        if a=='dir':
            b=l[0]
            curr[b]=curr.get(b,{})
        else:
            b=l[0]
            a=int(a)
            curr[b]=a

S=[0]
def f(d):
    r=0
    if type(d)==int:return d
    for c in d:
        if type(d[c])==int:
            r+=d[c]
        else:
            r+=f(d[c])
    if r<=100000:
        S[0]+=r
    S.append(r)
    return r

#part 1
total=f(d)
print(S[0])

#part 2
rem=30000000-(70000000-total)
print(min([v for v in S[1:] if v>=rem]))