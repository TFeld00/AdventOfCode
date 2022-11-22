DAY,_,_=__file__.rpartition('.')

from collections import *

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

#part 1
for c in zip(*r):
    print(end=Counter(c).most_common(1)[0][0])

print()

#part 2
for c in zip(*r):
    print(end=Counter(c).most_common(26)[-1][0])