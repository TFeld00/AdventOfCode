DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

r = parse_no_headers(r,int)

l=*map(sum,r),

print(max(l))

print(sum(sorted(l)[-3:]))