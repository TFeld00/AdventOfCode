import os
DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        pass

r_orig=r[:]

# Part 1
r=r_orig[:]
R=[]
while R!=r:
    R=r[:]
    for i,l in enumerate(r):
        s=''
        for j,c in enumerate(l):
            n=0
            for L in r[max(0,i-1):i+2]:
                for C in L[max(0,j-1):j+2]:
                    if C=='#':n+=1
            if c=='#':n-=1
            if c=='L' and n==0:
                s+='#'
            elif c=='#' and n>=4:
                s+='L'
            else:s+=c
        R[i]=s
    R,r=r[:],R[:]
print(sum(l.count('#')for l in r))


# Part 2
r=r_orig[:]

D={}
for i,l in enumerate(r):
    s=''
    for j,c in enumerate(l):
        X=[]
        for dx in -1,0,1:
            for dy in -1,0,1:
                if dx or dy:
                    x,y=j,i
                    C='.'
                    while C=='.':
                        x,y=x+dx,y+dy
                        if x<0 or y<0 or x>=len(r[0])or y>=len(r):break
                        C=r[y][x]
                        if C!='.':
                            X+=(y,x),;break
                    D[(i,j)]=X
R=[]
while R!=r:
    R=r[:]
    for i,l in enumerate(r):
        s=''
        for j,c in enumerate(l):
            n=0
            for y,x in D[(i,j)]:
                n+= r[y][x]=='#'
            if c=='L' and n==0:
                s+='#'
            elif c=='#' and n>=5:
                s+='L'
            else:s+=c
        R[i]=s
    R,r=r[:],R[:]
print(sum(l.count('#')for l in r))
