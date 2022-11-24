DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s=l

def f(L):
    x=s
    while len(x)<L:
        y=x[::-1].translate(str.maketrans('01','10'))
        x+='0'+y

    x=x[:L]
    while len(x)%2==0:
        x=''.join('01'[a==b] for a,b in zip(*[iter(x)]*2))
    return x

#part 1
print(f(272))

#part 2
print(f(35651584))