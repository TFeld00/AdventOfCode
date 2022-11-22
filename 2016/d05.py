DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s=l

from hashlib import md5

#part 1+2
p=''
d={}
i=0
while len(d)<8:
    h=md5(str.encode(s+str(i),'ascii')).hexdigest()
    if h[:5]=='0'*5:
        p+=h[5]
        if len(p)<9:
            print(p)
        if '0'<=h[5]<='7' and int(h[5])not in d:
            d[int(h[5])]=h[6]
            print(''.join(d.get(i,'_')for i in range(8)))
    i+=1

print()
print(p[:8])
print(''.join(d.get(i,'_')for i in range(8)))
