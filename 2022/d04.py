DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('\d+',l))]
        r+=[l]

s1=0
s2=0
for a,b,c,d in r:
    if a<=c<=d<=b or c<=a<=b<=d:s1+=1
    if (a<=c and b>=c) or (a<=d and b>=d) or (c<=a and d>=a) or (c<=b and d>=b):s2+=1

print(s1)
print(s2)