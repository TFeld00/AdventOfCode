DAY,_,_=__file__.rpartition('.')

from alg.util import  get_neigbors_orto

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
W,H=len(r[0]),len(r)

end=W-2,H-1

nodes={(1,0),(W-2,H-1)}
for i,l in enumerate(r[1:-1],1):
    for j,c in enumerate(l[1:-1],1):
        if r[i][j]!='#'and sum(v=='#' for _,_,v in get_neigbors_orto(r,i,j))<2:
            nodes|={(j,i)}

edges={}
for n in nodes:
    q=[(*n,0,{n})]
    for x,y,l,p in q:
        for X,Y,v in (x-1,y,'<.'),(x+1,y,'>.'),(x,y-1,'^.'),(x,y+1,'v.'):
            if (X,Y) not in p:
                if (X,Y)in nodes:
                    edges[n]=edges.get(n,[])+[((X,Y),l+1)]
                elif H>Y>=0<=X<W and r[Y][X]in v and (X,Y) not in p:
                    q+=[(X,Y,l+1,p|{(X,Y)})]


def getLongestPath(node, currSum):
    if V[node]:return
    V[node]=1

    if D.get(node,0) < currSum:
        D[node] = currSum

    for next,d in edges.get(node,[]):
        getLongestPath(next, currSum + d)

    V[node]=0
    
#part 1
D={}
V={n:0 for n in nodes}
getLongestPath((1,0),0)
print(D[end])

#part 2
for v in nodes:
    for w,d in edges.get(v,[]):
        edges[w]=edges.get(w,[])
        if (v,d)not in edges[w]:edges[w]+=(v,d),

D={}
V={n:0 for n in nodes}
getLongestPath((1,0),0)
print(D[end])