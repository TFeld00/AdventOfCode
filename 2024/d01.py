DAY,_,_=__file__.rpartition('.')


from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=[l]

a,b=zip(*r)

# Part 1
s=0
for x,y in zip(sorted(a),sorted(b)):
    s+=abs(y-x)
print(s)

# Part 2
s=0
for x in a:
    s+=x*b.count(x)
print(s)

