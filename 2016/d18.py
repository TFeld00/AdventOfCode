DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s=l

w=len(s)
n=[1]+[(c=='.')for c in s]+[1]
m=[1]+[0]*w+[1]
res=sum(n[1:-1])

for row in range(400000-1):
    for i in range(w):
        x=n[i]==n[i+2]
        m[i+1]=x
        res+=x
    n,m=m,n
    if row == 38:print(res) #part 1

#part 2
print(res)
