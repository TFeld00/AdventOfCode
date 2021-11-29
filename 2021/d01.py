DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        r+=int(l),
        
# PART 1
for i,a in enumerate(r):
    for b in r[i+1:]:
        if a+b==2020:print(a*b)
