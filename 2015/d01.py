DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

#part 1
print(s.count('(')-s.count(')'))

#part 2
l=0
for i,c in enumerate(s,1):
    if c=='(':l+=1
    else:l-=1
    if l<0:break
print(i)