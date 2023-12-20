DAY,_,_=__file__.rpartition('.')

from math import lcm, prod

from alg.file import download_input
download_input(DAY)

d={}

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.replace(',','')
        a,_,*l=l.split()
        d[a[1:]]=[a[0],l]
        
state={v:0 for v in d}
con={v:{} for v in d}
con['rx']={}
for v in d:
    for w in d[v][1]:
        if w in con:
            con[w][v]=0

a=[*con['rx'].keys()][0]
cycles={v:[] for v in con[a]}

sent=[0,0]
i=0
found=0
while not found:
    i+=1
    q=[['_','roadcaster',0]]
    for _,x,p in q:
        if i<=1000:
            sent[p]+=1
        if x in cycles and p==0:
            cycles[x]+=i,
            if all(len(v)>1 for v in cycles.values()):
                found=1
        if x not in d:continue

        t,l=d[x]
        if t=='%':
            if not p:
                state[x]^=1
                for v in l:
                    q+=[x,v,state[x]],
        elif t=='&':
            con[x][_]=p
            val=int(not all(con[x].values()))
            for v in l:
                q+=[x,v,val],
        else:
            for v in l:
                q+=[x,v,p],


#Part 1
print(prod(sent))
#Part 2
print(lcm(*[b-a for a,b in cycles.values()]))