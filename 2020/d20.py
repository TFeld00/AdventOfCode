import os
DAY,_,_=__file__.rpartition('.')

from img.img import read_img, write_img     #write_img(DAY,COLS)
import re
import sys

r=[]
s=0
tiles={}
n=''
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        if not l:
            x=n[5:-1]
            tiles[int(x)]=r
            n=''
            r=[]
            continue
        if l and not n:n=l
        elif n:
            r+=[l]

def ori(tile,i):
    if i==0:return tile
    if i==1:return[*zip(*tile)][::-1]
    if i==2:return[l[::-1] for l in tile[::-1]]
    if i==3:return[l[::-1]for l in zip(*tile)]
    tile=[*zip(*tile)]
    if i==4:return tile
    if i==5:return[*zip(*tile)][::-1]
    if i==6:return[l[::-1] for l in tile[::-1]]
    if i==7:return[l[::-1]for l in zip(*tile)]
    
def sides(t):
    r=[''.join(t[0])]
    z=[*zip(*t)]
    r+=[''.join(z[-1])]
    r+=[''.join(t[-1][::-1])]
    r+=[''.join(z[0][::-1])]
    return r
tiles2={}

for n,tile in tiles.items():
    s={}
    for i in range(8):
        t=ori(tile,i)
        s[i]=sides(t)
    tiles2[n]=s


if 0:
    x={0:2,1:3,2:0,3:1}
    E={}
    for n in tiles2:
        S=tiles2[n]
        for i in S:
            for j,s in enumerate(S[i]):
                for n2 in tiles2:
                    if n2==n:continue
                    for i2,s2 in tiles2[n2].items():
                        l=s2[x[j]]
                        if s==l[::-1]:
                            E[(n,i,j)]=E.get((n,i,j),[])+[(n2,i2)]

    E2={}
    for n,i,j in E:
        E2[n]=E2.get(n,{})
        E2[n][i]=E2[n].get(i,{})
        E2[n][i][j]=E[(n,i,j)]

    with open(f'd20_edges.txt','w')as F:
        for t in E2:
            F.write ('%r'%t+':'+str(E2[t])+',\n')
else:
    
    with open(f'd20_edges.txt','r')as F:
        s='{'
        for l in F:s+=l
        s+='}'
    E2=eval(s)


from queue import Queue

p=1
corners=[]
for t in E2:
    c=max(map(len,E2[t].values()))
    if c==2:
        p*=t
        corners+=[t]
print(p)

print(corners)

puz={}
p0=corners[0]
puz[(0,0)]=(p0,1)

q=Queue()
s=set()

q.put((0,0,p0,2,1))
q.put((0,0,p0,2,2))

delta={0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

N=10
while not q.empty() and N>0:
    x,y,t,i,s=q.get()
    for n,j in E2[t][i][s]:
        dx,dy=delta[s]
        X,Y=x+dx,y+dy
        if(X,Y)in puz:continue
        puz[(X,Y)]=(n,j)
        for s1 in range(4):
            if s1 in E2[n][j]:
                ddx,ddy=delta[s1]
                if (X+ddx,Y+ddy)not in puz:
                    q.put((X,Y,n,j,s1))
        break
    


Ro=[]
x,y=zip(*puz.keys())
for i in range(min(y),max(y)+1):
    l=[]
    for j in range(min(x),max(x)+1):
        t,o=puz[(j,i)]
        tile=[l[1:-1]for l in tiles[t][1:-1]]
        l+=[([*map(''.join,ori(tile,o))])]
    
    for r in zip(*l):        
        Ro+=''.join(r),

r1=[i for i,c in enumerate('                  # ')if c=='#']
r2=[i for i,c in enumerate('#    ##    ##    ###')if c=='#']
r3=[i for i,c in enumerate(' #  #  #  #  #  #   ')if c=='#']

S=(sum(l.count('#')for l in Ro))

for o in range(8):
    R=[*map(list,ori(Ro,o))]

    monster=0
    for y in range(len(R)-2):
        a1,a2,a3=R[y:y+3]
        for x in range(len(R[0])-len('                  # ')+1):
            if all(a1[x+i]=='#'for i in r1) and all(a2[x+i]=='#'for i in r2) and all(a3[x+i]=='#'for i in r3):
                monster+=1
                for i in r1:a1[x+i]='O'
                for i in r2:a2[x+i]='O'
                for i in r3:a3[x+i]='O'

    if monster:break
print(monster,S-monster*15)

with open(f'd20_map.txt','w')as F:
    for l in R:
        F.write (''.join(l)+'\n')


COLS = {
    '.': (0,0,0),
    '#': (0, 0, 200),
    'O': (100, 200, 0),
}

write_img('d20_map',COLS)
            