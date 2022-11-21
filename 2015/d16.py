DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

d={}

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        'Sue 37: samoyeds: 9, perfumes: 2, cars: 10'
        a,_,b=l.partition(': ')
        a=int(a[4:])
        D={}
        for v in b.split(', '):
            x,y=v.split(': ')
            D[x]=int(y)
        d[a]=D


R={
'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1
}

#part 1
for i,v in d.items():
    if all(R[x]==v[x] for x in v):
        print(i)

#part 2
def f(x,a,b):
    if x in ['cats','trees']:
        return a<b
    elif x in['pomeranians','goldfish']:
        return a>b
    else:
        return a==b

for i,v in d.items():
    if all(f(x,R[x],v[x]) for x in v):
        print(i)