DAY,_,_=__file__.rpartition('.')

from functools import cache

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        pass

cols = [c[2:-1]for c in zip(*r)][3::2]
cols=*zip('ABCD',cols),
top=(' ',)*11

def step_cost(c):
    return 10**'ABCD'.find(c)

def valid_from(c,col):
    r=any(' '!=x!=c for x in col)
    if r:
        for i,x in enumerate(col):
            if x!=' ':return i+1
    return 0

def valid_to(c,col):
    ri=0
    for i,x in enumerate(col):
        if ' '!=x!=c:return 0
        if x==' ':ri=i+1
    return ri

def get_col(cols,c):
    t={'A':0,'B':1,'C':2,'D':3}[c]
    return cols[t][1]

def can_move(i,c,top):
    t={'A':2,'B':4,'C':6,'D':8}[c]
    for j,v in enumerate(top):
        if (i<j<t or t<j<i) and v!=' ':return 0
    return 1

def done(cols):
    return all({k}=={*col}for k,col in cols)

def move(cols,top,i,c,v,c_top,c_col):
    T=[*top]
    T[i]=c_top
    Cd = {k:[*col]for k,col in cols}
    Cd[c][v-1]=c_col
    C=tuple((k,tuple(Cd[k]))for k in Cd)
    return tuple(C),tuple(T)


@cache
def f(cols,top):
    if done(cols):
        return 0,[]

    for i,c in enumerate(top):
        if c in'ABCD' and (v:=valid_to(c,get_col(cols,c))) and can_move(i,c,top):
            t={'A':2,'B':4,'C':6,'D':8}[c]
            dist = abs(t-i) + v
            cost = step_cost(c)*dist
            C,T=move(cols,top,i,c,v,' ',c)
            A,m=f(C,T)
            return cost + A, [*m, (cost,'v',(i,t))]
    
    result = 10**10
    M=[]
    for k,col in cols:
        v= valid_from(k,col)
        if not v:continue
        c=col[v-1]
        i={'A':2,'B':4,'C':6,'D':8}[k]
        for t,w in enumerate(top):
            if t in [2,4,6,8] or w!=' ':continue
            if can_move(t,k,top):
                dist = v+abs(t-i)
                cost = step_cost(c)*dist
                C,T=move(cols,top,t,k,v,c,' ')
                A,m=f(tuple(C),tuple(T))
                A+=cost
                if A<result:
                    result = A
                    M=[*m, (cost,'^',(i,t))]
    return result,M

#part 1
print(f(cols,top))

#part 2
ins="""  #D#C#B#A#
  #D#B#A#C#"""
r[3:3]=ins.split('\n')
cols=*zip('ABCD',[c[2:-1]for c in zip(*r)][3::2]),

print(f(cols,top)[0])