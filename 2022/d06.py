DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

for i in range(len(s)):
    if len(set(s[i:i+4]))==4:print(i+4);break

for i in range(len(s)):
    if len(set(s[i:i+14]))==14:print(i+14);break