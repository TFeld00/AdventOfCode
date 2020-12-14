import os
DAY,_,_=__file__.rpartition('.')

r_orig=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r_orig+=[l]
        pass

W,H=len(r_orig[0]),len(r_orig)

def get_neighbors(r,levels=1):
    D={}
    for i,l in enumerate(r):
        for j,c in enumerate(l):
            X=[]
            for dx in -1,0,1:
                for dy in -1,0,1:
                    if dx or dy:
                        x,y=j,i
                        depth=levels
                        while depth:
                            depth-=1
                            x,y=x+dx,y+dy
                            if not (0<=x<W and 0<=y<H):break
                            C=r[y][x]
                            if C!='.':
                                X+=(y,x),;break
                        D[(i,j)]=X
    return D

def getRules(part):
    if part==1:
        def rule(c,n):
            if c=='L' and n==0:
                return'#'
            elif c=='#' and n>=4:
                return'L'
            return c
        return rule
    if part==2:
        def rule(c,n):
            if c=='L' and n==0:
                return'#'
            elif c=='#' and n>=5:
                return'L'
            return c
        return rule


for part,level in (1,1),(2,-1):
    r=r_orig[:]
    D=get_neighbors(r,level)
    rule = getRules(part)

    R=[]
    while R!=r:
        R=r[:]
        for i,l in enumerate(r):
            s=''
            for j,c in enumerate(l):
                n=0
                for y,x in D[(i,j)]:
                    n+=r[y][x]=='#'
                s+=rule(c,n)
            R[i]=s
        R,r=r[:],R[:]
    print(sum(l.count('#')for l in r))
