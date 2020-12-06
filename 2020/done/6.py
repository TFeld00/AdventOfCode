import os
DAY,_,_=__file__.rpartition('.')

r=[]
p=set()
a=1
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        if l:
            # PART 1
            #p |={*l}
            
            # PART 2
            if a:p={*l};a=0
            p &={*l}
        else:
            r += p,
            p = set()
            a=1
r+=p
print (sum(map(len,r)))

