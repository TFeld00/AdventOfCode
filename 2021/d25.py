DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]

def move(m):
    M=[]
    for i,l in enumerate(m):
        L=l[:]
        for j,c in enumerate(l):
            J=(j+1)%len(l)
            if c=='>' and l[J]=='.':
                L[J]=c
                L[j]='.'
        M+=L,
    M2=[l[:]for l in M]
    for i,l in enumerate(M):
        for j,c in enumerate(l):
            I=(i+1)%len(M)
            if c=='v' and M[I][j]=='.':
                M2[I][j]=c
                M2[i][j]='.'
    return M2

s=0
while 1:
    a=move(r)
    s+=1
    if a==r:break
    r=a
print(s)