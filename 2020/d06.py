import os
DAY,_,_=__file__.rpartition('.')
from string import ascii_lowercase

r=[]
p=set(ascii_lowercase)
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        if l:
            # PART 1
            #p |={*l}
            
            # PART 2
            p &={*l}
        else:
            r += p,
            p = set(ascii_lowercase)
r+=p
print (sum(map(len,r)))

