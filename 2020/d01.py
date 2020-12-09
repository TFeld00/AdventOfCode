r=[]
DAY,_,_=__file__.rpartition('.')

with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        r+=int(l),
        
# PART 1
for i,a in enumerate(r):
    for b in r[i+1:]:
        if a+b==2020:print(a*b)


# PART 2
for i,a in enumerate(r):
    for j,b in enumerate(r[i+1:],i+1):
        for c in r[j+1:]:
            if a+b+c==2020:print(a*b*c)

