DAY,_,_=__file__.rpartition('.')

from itertools import *

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s=l

for i in range(40):
    s=''.join(str(len(list(g)))+c for c,g in groupby(s))
print(len(s))

for i in range(10):
    s=''.join(str(len(list(g)))+c for c,g in groupby(s))
print(len(s))