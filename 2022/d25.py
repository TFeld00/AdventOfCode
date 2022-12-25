DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

def parse(s):
    n=0
    for c in s:
        n*=5
        n+='=-012'.find(c)-2
    return n

def tos(n):
    s=''
    while n:
        v=n%5
        s='012=-'[v%5]+s
        if v>2:n+=5
        n//=5
    return s

l=[*map(parse,r)]
print(tos(sum(l)))