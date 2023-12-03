DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

sym={*''.join(r)}-{*'.1234567890'}
s=0
d={}
for i,l in enumerate(r):
    j=0
    while j<len(l):
        n=''
        x=j
        while j<len(l) and l[j].isdigit():j+=1
        if j>x:
            n=l[x:j]
            v=''
            for di in range(max(0,i-1),min(len(r),i+2)):
                # Part 1
                v+=r[di][max(0,x-1):j+1]
                # Part 2
                for J in range(max(0,x-1),min(len(l),j+1)):
                    if r[di][J]=='*':
                        d[(di,J)]=d.get((di,J),[])+[int(n)]
            #Part 1
            if sym & {*v}:
                s+=int(n)
        else:
            j+=1
        

print(s)

#Part 2
s2=0
for v in d:
    l=d[v]
    if len(l)>1:
        p=1
        for v in l:
            p*=v
        s2+=p
print(s2)