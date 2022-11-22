DAY,_,_=__file__.rpartition('.')

from alg.string import block_print

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

s=[[0]*50 for _ in range(6)]
for o,*l in r:
    if o=='rect':
        a,b=map(int,l[0].split('x'))
        for i in range(b):
            s[i][:a]=[1]*a
    elif o=='rotate':
        o,a,_,b = l
        a=int(a[2:])
        b=int(b)
        if o=='row':
            b%=50
            s[a] = s[a][-b:]+s[a][:-b]
        else:
            b%=6
            s=[*zip(*s)]
            s[a] = s[a][-b:]+s[a][:-b]
            s=[*map(list,zip(*s))]

#part 1
print(sum(map(sum,s)))

#part 2
block_print(s)