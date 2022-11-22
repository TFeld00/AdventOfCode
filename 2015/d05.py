DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

#part 1
n=0
for s in r:
    if len(re.findall(r'[aeiou]',s))>=3 and re.search(r'(.)\1',s) and (not re.search(r'ab|cd|pq|xy',s)):
        n+=1
print(n)

#part 2
n=0
for s in r:
    if re.search(r'(..).*\1',s) and re.search(r'(.).\1',s):
        n+=1
print(n)
