DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        n=int(l)

#part 1
d=[0]*(n//10)

for i in range(1,n//10):
    for j in range(i,n//10,i):
        d[j]+=i
for i in range(len(d)):
    if d[i]*10>=n:
        break
print(i)

#part 2
d=[0]*(n//10)

for i in range(1,n//10):
    for j in range(i,min(i*50+1,n//10),i):
        d[j]+=i
for i in range(len(d)):
    if d[i]*11>=n:
        break
print(i)
