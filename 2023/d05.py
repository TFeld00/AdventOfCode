DAY,_,_=__file__.rpartition('.')

from alg.util import parse_skip_headers

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a=r[0]
seed=[*map(int,a.split()[1:])]

D=parse_skip_headers(r[2:], lambda s:[*map(int,s.split())])

#Part 1
inp=seed
for ss in D:
    out = []
    for v in inp:
        x=v
        for d,s,l in ss:
            if v in range(s,s+l):
                x=d+(v-s)
        out+=x,
    inp=out
print(min(inp))

#Part 2
seed = [*zip(*[iter(seed)]*2)]
inp=[[a,a+b-1]for a,b in seed]
for ss in D:
    out = []
    for a,A in inp:
        u=[]
        for d,s,l in ss:
            S=s+l-1
            if a<=S and s<=A:
                out += [d+(max(s,a)-s),d+(min(S,A)-s)],
                u+=[(max(s,a)),(min(S,A))+1],
        for b,B in sorted(u+[[A+1,A+1]]): # Add missing intervals
            if b>a:
                c,C=a,b-1
                out+=[c,C],
            a,A=B,A
    inp=out
print(min(inp)[0])